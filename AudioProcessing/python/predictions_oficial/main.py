# Mostrar propriedades importantes do predictor

# Pegar sinal de audio
# Fazer a predicao com ele
# Plottar dee
# Plottar dee do erro
# Calcular Prediction Error Gain
# Plotar DEE's
# Mostrar resultados para diferentes n's

from record_audio import load_audio_to_numpy, plot_audio
from autocorrelation import compute_autocorrelation, plot_autocorrelation
import numpy as np
import matplotlib.pyplot as plt
from prediction import compute_prediction_error_gain, plot_prediction_and_error_custom_ax, predict_signal
from psd import plot_psds
from H_pef import compute_H, plot_H, plot_H_custom_ax, plot_H_inverse, plot_H_inverse_smoothed_custom_ax
import math
from scipy.signal import windows


audio_data = load_audio_to_numpy('e.wav')
random_index = np.random.randint(1, len(audio_data) - 10000)
audio_data = audio_data[random_index:random_index + 10000]

N_samples = len(audio_data)

sample_rate = 44100

# Vou fazer um preditor com ordem de 16
N_order = [10, 12, 16, 128]

# rxx = compute_autocorrelation(audio_data, N) # Vai de 0 a N - N+1 elementos
prediction = predict_signal(audio_data, N_order[0])
error = audio_data - prediction

# plot_psds([10, 100, 200, 500, 1000])

# Agora vamos tentar calcular o modelo paramétrico do envelope espectral
# Hinv PEF

# plot_H(audio_data, error, sample_rate, show_every=128)
eps = 1e-10
freqs, H = compute_H(audio_data, error, sample_rate)
H_inv = np.ones_like(len(H)) / (H+eps)  # Inverso do envelope espectral
# plot_H_inverse(audio_data, error, sample_rate, show_every=16)


# H_inv_smoothed = np.copy(H_inv)
# neighbours = 200
# for i in range(neighbours, len(H_inv) - neighbours):
#     for j in range(1, neighbours + 1):
#         H_inv_smoothed[i] += H_inv[i - j] + H_inv[i + j]
# H_inv = H_inv_smoothed

# Normalize the smoothed signal to have the same scale as the original
smoothed_H_inv = np.convolve(H_inv, windows.hann(80), mode='same')
smoothed_H_inv *= np.sum(H_inv) / np.sum(smoothed_H_inv)


H_inv_db_smoothed = 20 * np.log10(smoothed_H_inv)
H_inv_db = 20 * np.log10(H_inv)

# plt.figure()
# plt.title('Envelope Espectral Inverso')
# plt.plot(freqs, H_inv_db, alpha=0.7)
# plt.plot(freqs, H_inv_db_smoothed)
# plt.xlabel('Frequência (Hz)')
# plt.ylabel('Magnitude (dB)')
# plt.grid()
# plt.show()

def plot_all():
    fig, axs = plt.subplots(3, 2, figsize=(10, 5))
    plot_audio(audio_data, axs[0, 0], 'Sinal Original')
    plot_autocorrelation(audio_data, N_order[0], axs[0, 1])
    plot_psds(audio_data, N_order, axs[1, 0])
    plot_prediction_and_error_custom_ax(audio_data, N_order[0], axs[1, 1])
    plot_H_custom_ax(audio_data, error, sample_rate, show_every=1, ax=axs[2, 0])
    plot_H_inverse_smoothed_custom_ax(audio_data, error, sample_rate, axs[2, 1], show_every=1, fmax=5000)

    plt.tight_layout()
    plt.show()

plot_all()