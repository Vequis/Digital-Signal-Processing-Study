import numpy as np
import matplotlib.pyplot as plt
import time

def compute_autocorrelation(signal, N, print_time=False):
    """
    Compute the autocorrelation vector for k = 0, 1, ..., N.
    """
    start_time = time.time()

    n = len(signal)
    print('n:', n, " ;N:", N)
    rxx = np.zeros(N + 1)
    for lag in range(N + 1):
        x = signal[:n - lag] * signal[lag:]
        rxx[lag] = np.sum(x)
        rxx[lag] /= len(x)

    end_time = time.time()
    if print_time:
        print(f"Execution time: {end_time - start_time} seconds")
    return rxx

# compute_autocorrelation using np.correlate
def compute_autocorrelation_np(signal,N, print_time=False):
    # Aparentemente, essa função é MUITO mais lenta que a anterior
    start_time = time.time()
    
    N_samples = len(signal)
    result = np.correlate(signal, signal, mode='full')[N_samples-1:N_samples+N] / np.arange(N_samples, N_samples - N - 1, -1)
    
    end_time = time.time()
    if print_time:
        print(f"Execution time with np.corr: {end_time - start_time} seconds")
    
    return result

def plot_autocorrelation(signal, N, ax):
    rxx_full = compute_autocorrelation(signal, N)
    ax.plot(rxx_full)
    ax.set_title('Autocorrelation using custom function')
    ax.set_xlabel('Lag')
    ax.set_ylabel('Autocorrelation')
    ax.grid()


# Never use autocorrelation_cyclic (haha)
# plt.figure()

# plt.subplot(211)
# plt.plot(t, sinal)
# plt.xlabel('Tempo (s)')
# plt.ylabel('Amplitude')
# plt.grid()

# plt.subplot(212)
# plt.plot(autocorrelation)
# plt.plot(autocorrelation_np[599:], linestyle='--')
# plt.xlabel('Lag')
# plt.ylabel('Autocorrelação')
# plt.grid()

# plt.tight_layout()
# plt.show()