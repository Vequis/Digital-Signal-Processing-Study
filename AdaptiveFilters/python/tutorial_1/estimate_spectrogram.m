%ESTIMATE_SPECTROGRAM Calculate the spectrogram of a signal.
%
%   X = calculate_spectrogram(x) calculates the spectrum(spectrogram) 
%       of a signal x.
%
%   INPUT
%   x       - Signal
%   N_fft   - FFT resolution (optional)
%   frameshift  - Number of samples between signal blocks. (optional)
%
%   OUTPUT
%   X       - Spectrogram
%
function [X] = estimate_spectrogram(x, N_fft, frameshift)

    % Set default values.
    if nargin < 3, N_fft = 256; end
    if nargin < 4, frameshift = 64; end

    %Compute Hanning window with window length
    h_win = hanning(N_fft);
    
    %Calculate spectrogram with window(h_win), overlap(N_fft-frameshift) and
    %FFT length(N_fft) 
    X = spectrogram(x, h_win, N_fft-frameshift, N_fft);
end