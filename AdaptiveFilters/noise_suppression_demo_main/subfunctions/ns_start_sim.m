function ns_start_sim;

main_data = get(gcf,'UserData');

%**************************************************************************
% Generate noise with appropriate power
%**************************************************************************
main_data.signals.b_temp = 10^(-main_data.signals.SNR/20) * main_data.signals.b;
main_data.signals.y      = main_data.signals.s + main_data.signals.b_temp;

%**************************************************************************
% Window function
%**************************************************************************
h_win = hanning(main_data.N_FFT,'periodic');
h_win = h_win / sqrt(sum(h_win.^2) / main_data.frameshift);

%**************************************************************************
% Spectrogram of the noisy input signal
%**************************************************************************
main_data.signals.Specgram_y = spectrogram(main_data.signals.y,h_win, ...
                                           main_data.N_FFT-main_data.frameshift, ...
                                           main_data.N_FFT);

%**************************************************************************
% Estimation of power spectral density of the noise
%**************************************************************************                                     
main_data.signals.Specgram_b_temp =  spectrogram(main_data.signals.b_temp,h_win, ...
                                           main_data.N_FFT-main_data.frameshift, ...
                                           main_data.N_FFT);       
S_bb = mean(abs(main_data.signals.Specgram_b_temp).^2,2);                                       
S_bb = S_bb * main_data.overest;          
          
%**************************************************************************
% Compute the output spectrogram
%**************************************************************************
[N_f, N_t]                        = size(main_data.signals.Specgram_y);
main_data.signals.Specgram_s_dach = zeros(size(main_data.signals.Specgram_y));

att_lin = 10^(-main_data.max_att/20);
for k=1:N_t
    H_wiener = max(att_lin, 1 - S_bb./abs(main_data.signals.Specgram_y(:,k)).^2);
    main_data.signals.Specgram_s_dach(:,k) = main_data.signals.Specgram_y(:,k) .* H_wiener;                 
end;
   
%**************************************************************************
% Compute the output signal
%**************************************************************************
main_data.signals.s_dach = zeros(size(main_data.signals.y));
for k=1:N_t
   main_data.signals.s_dach(1+(k-1)*main_data.frameshift:main_data.N_FFT+(k-1)*main_data.frameshift) = ...
     main_data.signals.s_dach(1+(k-1)*main_data.frameshift:main_data.N_FFT+(k-1)*main_data.frameshift) ...
     + real(ifft([main_data.signals.Specgram_s_dach(:,k);conj(main_data.signals.Specgram_s_dach(end-1:-1:2,k))])) ...
     .* h_win;
end;

set(gcf,'UserData',main_data);


ns_plot_init(1);  
ns_plot_init(2);  