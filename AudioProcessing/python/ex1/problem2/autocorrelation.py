import numpy as np

def compute_autocorrelation(signal, N):
    """
    Compute the autocorrelation vector for k = 0, 1, ..., N.
    """
    n = len(signal)
    rxx = np.zeros(N + 1)
    for lag in range(N + 1):
        x = signal[:n - lag] * signal[lag:]
        rxx[lag] = np.sum(x) / len(x)
    
    return rxx

def plot_autocorrelation(signal, N, ax):
    rxx_full = compute_autocorrelation(signal, N)
    ax.plot(rxx_full)
    ax.set_title('Autocorrelation using custom function')
    ax.set_xlabel('Lag')
    ax.set_ylabel('Autocorrelation')
    ax.grid()