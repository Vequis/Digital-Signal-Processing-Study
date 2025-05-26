%PLOT_PSD Plot a given power spectral density(PSD) 
%                   
%
%   plot_PSD(S_xx,Fs) plots a given PSD 
%
%   INPUT
%   S_xx    - a PSD
%   Fs      - Sampling Frequency of the signal used to calculate the PSD
%   N_fft   - FFT resolution (optional)
%   frameshift  - Number of samples between signal blocks. (optional)
%
function plot_PSD(S_xx, Fs, N_fft, frameshift)

    %Set default values.
    if nargin < 3, N_fft = 256; end
    if nargin < 4, frameshift = 64; end

    [N_f, N_t] = size(S_xx);

    signal_length = N_t * frameshift;
    signal_length/Fs

    %Frequency (y-axis)
    F = [1/N_f:1/N_f:1]*Fs/2;
    %Time (x-axis)
    T = [N_fft/2:frameshift:signal_length-N_fft/2]/Fs;

    %Plot the PSD
    figure;
    imagesc(T, F, 10*log10(S_xx));
    colorbar;
    set(gca,'YDir', 'normal'); %switch the y-axis
    ylabel('Frequency [Hz]');
    xlabel('Time [s]');
end