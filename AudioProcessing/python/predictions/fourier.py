import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# print(plt.style.available)
# plt.style.use('ggplot')

N_samples = 1000
t = np.linspace(0, 1, N_samples, endpoint=False)
sinal = np.sin(2 * np.pi * 2 * t) + 0.5 * np.sin(2 * np.pi * 4 * t)
ruido = np.random.normal(0, 0.3, N_samples)  # Ruído gaussiano branco com média 0 e desvio padrão 0.1
sinal_com_ruido = sinal + ruido
sinal = sinal_com_ruido

def my_dft():
    N = len(sinal)

    X = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        for k in range(N):
            X[n] += sinal[k] * np.exp(-1j * 2 * np.pi * k * n / N)
    return X



plt.figure()
plt.subplot(211)
plt.plot(t, sinal, label='Sinal Original')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid()

# X = my_dft()
X = np.fft.fft(sinal)
plt.subplot(212)
plt.stem(np.abs(X))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()
