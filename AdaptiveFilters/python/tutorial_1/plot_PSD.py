import numpy as np
import matplotlib.pyplot as plt

def plot_PSD(S_xx, Fs, N_fft=256, frameshift=64):
    """
    PLOT_PSD Plot a given power spectral density (PSD)
    
    plot_PSD(S_xx, Fs) plots a given PSD

    Parameters:
    S_xx        -- a PSD
    Fs          -- Sampling Frequency of the signal used to calculate the PSD
    N_fft       -- FFT resolution (optional)
    frameshift  -- Number of samples between signal blocks (optional)
    """

    N_f, N_t = S_xx.shape

    signal_length = N_t * frameshift
    print(signal_length / Fs)

    #Frequency (y-axis)
    F = np.linspace(1/N_f, 1, N_f) * Fs / 2
    #Time (x-axis)
    T = np.arange(N_fft/2, signal_length - N_fft/2 + 1, frameshift) / Fs

    #Plot the PSD
    plt.figure()
    plt.imshow(10 * np.log10(S_xx), aspect='auto', extent=[T[0], T[-1], F[0], F[-1]], origin='lower')
    plt.colorbar()
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.show()
