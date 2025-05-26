import numpy as np
from scipy.fft import fft, ifft
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

N_samples = 1000
t = np.linspace(0, 0.001 * N_samples, N_samples, endpoint=False)
# sinal = sinal_com_ruido


#sinal com freq menor
sinal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
# sinal = np.sin(2 * np.pi * 50 * t)
sinal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
ruido = np.random.normal(0, 1, N_samples)  # Ruído gaussiano branco com média 0 e desvio padrão 0.1
sinal_com_ruido = sinal + ruido

# Primeiro, vamos fazer o predictor considerando os primeiros coeficientes = 0

N = 20

def calculate_autocorrelation(signal):
    autocorrelation = np.zeros(N)
    for k in range(N):
        for n in range(N-k):
            autocorrelation[k] += signal[n] * signal[(n + k)%N]
        autocorrelation[k] /= (N-k)
    return autocorrelation


def predictor(last_values):
    autocorrelation = calculate_autocorrelation(last_values)
    # autocorrelation = np.correlate(last_values, last_values, mode='full')
    R = np.zeros((N, N))

    for i in range(N):
        for j in range(N):
            R[i, j] = autocorrelation[np.abs(i-j)]

    R = np.linalg.pinv(R)
    r = autocorrelation[1:N]
    # r = np.append(r, autocorrelation[0])
    r = np.append(r, 0)
    return R@r
    

prediction = np.zeros(N_samples)
for i in range(N_samples):
    if i < N:
        prediction[i] = sinal[i]
    else:
        soma = 0
        coefs = predictor(sinal[i-N:i])
        for j in range(N):
            soma += sinal[i-j-1]*coefs[j]
        # print(soma)
        # prediction[i] = np.dot(sinal[i-N:i], predictor(sinal[i-N:i]))
        # print(prediction[i])
        prediction[i] = soma

error = np.abs(sinal - prediction)

plt.figure()
plt.plot(t, sinal, label='Sinal Original')
plt.plot(t, prediction, label='Predição')
# plt.plot(t, error, label='Erro', linestyle='--', color='red')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Predição do Sinal')
plt.legend()
plt.show()
