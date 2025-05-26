%CALCULATE_OUTPUT Calculate the output of the Wiener filter
%
%   s_hat = calculate_output(S_hat,size_y) transforms the output of the 
%           Wiener filter in the time domain    
%
%   INPUT
%   S_hat   - Spectra(spectrogram) of the output of Wiener filter
%   size_y  - Dimensions of the noisy signal
%   N_fft   - FFT resolution (optional)
%   frameshift  - Number of samples between signal blocks. (optional)
%
%   OUTPUT
%   s_hat   - Output of Wiener filter in time domain
%
function s_hat = calculate_output(S_hat, size_y, N_fft, frameshift)

    % Set default values.
    if nargin < 3, N_fft = 256; end
    if nargin < 4, frameshift = 64; end

    [N_f, N_t] = size(S_hat);
    
    % Initialization of s_hat
    s_hat = zeros(size_y);
    
    % Transformation from frequency domain to time domain 
    for k=1:N_t
        frame = real(ifft([S_hat(:,k);conj(S_hat(end-1:-1:2,k))]))*frameshift/(N_fft/2);
        s_hat(1+(k-1)*frameshift:N_fft+(k-1)*frameshift) = s_hat(1+(k-1)*frameshift:N_fft+(k-1)*frameshift) ...
                                                         + frame;
    end
end