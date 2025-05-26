# CONCLUSÃO
# Utilize plt.psd 
#
# Mais simples de implementar e retorna uma função mais suave
# por conta de janelamentos
# Essa vai dar errado pq autocorrelation.py ta cagado

from record_audio import load_audio_to_numpy
from autocorrelation import compute_autocorrelation
from prediction import predict_signal, compute_prediction_error_gain
import numpy as np
import math
import matplotlib.pyplot as plt


audio_data = load_audio_to_numpy('e.wav')
audio_data = audio_data[80000:120000]

def calculate_psd(signal):
    N_samples = len(signal)
    fft_values = np.fft.fft(signal)
    power_spectrum = np.abs(fft_values) ** 2

    psd = power_spectrum / N_samples

    freqs = np.fft.fftfreq(N_samples, 1 / 44100)
    positive_freqs = freqs[:N_samples // 2]
    psd = psd[:N_samples // 2]

    return positive_freqs, psd

def plot_to_show_differences():
    rxx_full = compute_autocorrelation(audio_data, len(audio_data))

    plt.figure()
    plt.subplot(311)
    plt.plot(rxx_full)
    plt.subplot(312)
    plt.plot(calculate_psd(audio_data))
    plt.yscale('log')
    plt.grid()
    plt.subplot(313)
    plt.psd(audio_data, NFFT=len(audio_data), Fs=44100)

    plt.tight_layout()
    plt.show()

def plot_psds(signal, range, ax=None):
    N_samples = len(signal)
    if ax is None:
        plt.figure()
        ax = plt.gca()
    
    ax.psd(audio_data, NFFT=N_samples//8, Fs=44100, label='Original signal')
    ax.set_title(f'Error signal: prediction order = {range}')
    for N in range:
        prediction = predict_signal(audio_data, N)
        error = audio_data - prediction

        # PREDICTION ERROR GAIN
        # Está diretamente relacionado com o quão mais "branco" é a DEP do erro
        peg = compute_prediction_error_gain(audio_data, N)
        peg_db = 10 * math.log10(peg)
        
        ax.psd(error, NFFT=N_samples//32, Fs=44100, label=f'Error with N = {N}, peg = {peg_db:.2f} dB')

    ax.legend()
    if ax is plt.gca():
        plt.show()

