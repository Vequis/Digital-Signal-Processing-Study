import numpy as np
from scipy.fft import fft, ifft
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

N = 600
t = np.linspace(0, 0.001*N, N, endpoint=False)
sinal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

def calculate_autocorrelation(signal):
    N = len(signal)
    autocorrelation = np.zeros(N)
    for k in range(N):
        for n in range(N - k):
            autocorrelation[k] += signal[n] * signal[n + k]
        autocorrelation[k] /= (N-k)
    return autocorrelation

autocorrelation = calculate_autocorrelation(sinal)

def calculate_autocorrelation_np(signal):
    return np.correlate(signal, signal, mode='full')


autocorrelation_np = calculate_autocorrelation_np(sinal)
print(len(autocorrelation_np))

def calculate_autocorrelation_cyclic(signal):
    N = len(signal)
    autocorrelation = np.zeros(N)
    for k in range(N):
        for n in range(N):
            autocorrelation[k] += signal[n] * signal[(n + k) % N]
    return autocorrelation

autocorrelation_cyclic = calculate_autocorrelation_cyclic(sinal)

plt.figure()

plt.subplot(211)
plt.plot(t, sinal)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(212)
plt.plot(autocorrelation)
plt.plot(autocorrelation_np[599:], linestyle='--')
plt.xlabel('Lag')
plt.ylabel('Autocorrelação')
plt.grid()

plt.tight_layout()
plt.show()