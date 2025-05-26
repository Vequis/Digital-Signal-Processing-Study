import numpy as np
from scipy.signal import get_window, stft

def estimate_STFT(x, N_fft=256, frameshift=64):
    """
    ESTIMATE_STFT Calculate the STFT of a signal.

    X = estimate_STFT(x) calculates the spectrum (STFT) 
    of a signal x.

    Parameters:
    x           -- Signal
    N_fft       -- FFT resolution (optional)
    frameshift  -- Number of samples between signal blocks (optional)

    Returns:
    X           -- STFT (STFT)
    """

    #Compute Hanning window with window length
    h_win = get_window('hann', N_fft)

    #Calculate STFT with window(h_win), overlap(N_fft-frameshift) and
    #FFT length(N_fft) 

    # spectrogram from scipy actually calculates the periodogram
    # and now we just want the STFT
    f, t, X = stft(x, window=h_win, noverlap=N_fft - frameshift, nfft=N_fft, mode='complex')

    return f, t, X
