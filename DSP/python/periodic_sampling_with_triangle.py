import numpy as np
import matplotlib.pyplot as plt

rate = 1000 # Amostras / segundo
samples = 1000 # Número de amostras

# t vai representar 1 segundo
# Com separação de 1 ms entre amostras
t = np.linspace(0, samples, rate)
x = np.zeros_like(t)
X = np.fft.fft(x)
X = np.abs(X)

# se f_max > fa/2, o sinal não pode ser recuperado
f_max = 75 # Hz

fa = 100 # Hz /// (fa / 2) = 50Hz
Ta = 1/fa
amostras_por_periodo = int(Ta * rate) # s * Hz = amostras


# TREM DE IMPULSOS
impulse_train = np.zeros(rate)
impulse_train[::amostras_por_periodo] = 1 # Pegar uma amostra a cada amostras_por_periodo amostras


# GERANDO SINAL TRIANGULAR NA FREQUÊNCIA
for w in range(f_max): # i é o w (frequência)
    if (w != 0): x += np.cos(t*(2*np.pi*w)) * (f_max - w) # Criar um formato de triângulo na frequência
    else: x += f_max/2 # Adicionar a componente de frequência 0

xc = x * impulse_train

plt.figure()
plt.subplot(321)
plt.plot(t, x)
plt.subplot(322)
plt.plot(X)
plt.subplot(323)
plt.plot(xc)
plt.subplot(324)
plt.plot(np.abs(np.fft.fft(xc)))
plt.subplot(325)
plt.plot(impulse_train)
plt.tight_layout()
plt.show()