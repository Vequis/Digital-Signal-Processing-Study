import numpy as np
from scipy.fft import fft, ifft
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Criar arrays
x = np.array([1, 2, 3, 4])
y = np.linspace(0, 10, 100)  # 100 pontos entre 0 e 10
z = np.zeros(10)             # Vetor de zeros
w = np.ones(10)              # Vetor de uns

# Operações básicas
soma = x + y[:4]             # Soma de arrays
produto = x * 2              # Multiplicação escalar
matriz = np.array([[1, 2], [3, 4]])
inversa = np.linalg.inv(matriz)  # Inversão de matriz 2x2



# Sinal de exemplo
t = np.linspace(0, 1, 1000, endpoint=False) # de 0 a 1 com 1000 pontos
print(t)
sinal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# FFT e IFFT
sinal_fft = fft(sinal)
sinal_recuperado = ifft(sinal_fft)

freqs = np.fft.fftfreq(len(sinal), 1/1000)
# plt.plot(freqs, np.abs(sinal_fft))
# plt.title('Espectro de Frequência')
# plt.xlabel('Frequência (Hz)')
# plt.ylabel('Amplitude')
# plt.show()



# Filtro passa-baixa de exemplo
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order)
    y = lfilter(b, a, data)
    return y

# Filtrando um sinal
filtered_signal = lowpass_filter(sinal, cutoff=60, fs=1000)


tc = 0.2
plt.figure()
# Primeiro subplot (sinal original)
# plt.subplot(2, 1, 1)
plt.plot(t[t < tc], sinal[t < tc], label='Sinal Original')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal Original')
plt.grid(True)

# Segundo subplot (sinal filtrado)
# plt.subplot(2, 1, 2)
plt.plot(t[t < tc], filtered_signal[t < tc], label='Sinal Filtrado', color='orange', linestyle='--')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal Filtrado')
plt.grid(True)

# Ajusta o layout e exibe a figura
plt.tight_layout()
plt.show()

