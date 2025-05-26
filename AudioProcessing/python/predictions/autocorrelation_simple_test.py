import numpy as np

N = 5
N_samples = 10

def compute_autocorrelation(signal):
    """
    Compute the autocorrelation vector for k = 0, 1, ..., N.
    """
    n = len(signal)
    print('n:', n, " ;N:", N)
    rxx = np.zeros(N + 1)
    for lag in range(N + 1):
        x = signal[:n - lag] * signal[lag:]
        rxx[lag] = np.sum(x)
        rxx[lag] /= len(x)
    return rxx

# compute_autocorrelation using np.correlate
def compute_autocorrelation_np(signal):
    return np.correlate(signal, signal, mode='full')[N_samples-1:N_samples+N] / np.arange(N_samples, N_samples - N - 1, -1)
    # 0 -> N-1
    # N -> 2N-1

signal = np.ones(10)

print(compute_autocorrelation(signal))
print(compute_autocorrelation_np(signal))
