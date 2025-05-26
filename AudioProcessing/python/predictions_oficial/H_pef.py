import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import windows

def compute_H(x, y, sample_rate):


    X = np.fft.fft(x)
    Y = np.fft.fft(y)
    
    # Avoid division by zero by adding a small epsilon to Y
    epsilon = 1e-12
    H_pef = X / (Y + epsilon)
    
    # Compute the corresponding frequencies
    freqs = np.fft.fftfreq(len(x), 1 / sample_rate)
    positive_freqs = freqs[:len(freqs) // 2]
    H_pef_magnitude = np.abs(H_pef[:len(freqs) // 2])
    
    return positive_freqs, H_pef_magnitude

def plot_H(x, y, sample_rate, show_every=1):
    freqs, H_pef = compute_H(x, y, sample_rate)
    H_pef_db = 20 * np.log10(H_pef)
    
    freqs = freqs[::show_every]
    H_pef_db = H_pef_db[::show_every]
    plt.figure()
    plt.plot(freqs, H_pef_db)
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid()
    plt.show()

def plot_H_custom_ax(x, y, sample_rate, ax, show_every=1):
    freqs, H_pef = compute_H(x, y, sample_rate)
    H_pef_db = 20 * np.log10(H_pef)
    
    freqs = freqs[::show_every]
    H_pef_db = H_pef_db[::show_every]
    ax.plot(freqs, H_pef_db)
    ax.set_xlabel('Frequência (Hz)')
    ax.set_ylabel('Magnitude (dB)')
    ax.title.set_text('H_pef')
    ax.grid()

def plot_H_inverse(x, y, sample_rate, show_every=1, fmax=5000):
    freqs, H_pef = compute_H(x, y, sample_rate)
    
    H_inv = 1 / H_pef
    H_inv_db = 20 * np.log10(H_inv)

    # Filter frequencies up to fmax
    mask = freqs <= fmax
    freqs = freqs[mask][::show_every]
    H_inv_db = H_inv_db[mask][::show_every]

    plt.figure()
    plt.plot(freqs, H_inv_db)
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid()
    plt.show()

def plot_H_inverse_smoothed_custom_ax(x, y, sample_rate, ax, show_every=1, fmax=5000):
    freqs, H_pef = compute_H(x, y, sample_rate)
    
    H_inv = 1 / H_pef
    
    smoothed_H_inv = np.convolve(H_inv, windows.hann(80), mode='same')
    smoothed_H_inv *= np.sum(H_inv) / np.sum(smoothed_H_inv)

    H_inv_db = 20 * np.log10(H_inv)
    H_inv_db_smoothed = 20 * np.log10(smoothed_H_inv)

    # Filter frequencies up to fmax
    mask = freqs <= fmax
    freqs = freqs[mask][::show_every]
    H_inv_db = H_inv_db[mask][::show_every]
    H_inv_db_smoothed = H_inv_db_smoothed[mask][::show_every]

    ax.plot(freqs, H_inv_db, alpha=0.7)
    ax.plot(freqs, H_inv_db_smoothed)
    ax.set_xlabel('Frequência (Hz)')
    ax.set_ylabel('Magnitude (dB)')
    ax.title.set_text('Spectral Envelope')
    ax.grid()