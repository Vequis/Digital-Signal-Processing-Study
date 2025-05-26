# CONCLUSÃO
# Utilize plt.psd 
#
# Mais simples de implementar e retorna uma função mais suave
# por conta de janelamentos
# Essa vai dar errado pq autocorrelation.py ta cagado

from record_audio import load_audio_to_numpy
from autocorrelation import calculate_autocorrelation
import numpy as np
import matplotlib.pyplot as plt
audio_data = load_audio_to_numpy('e.wav')
audio_data = audio_data[80000:120000]

# Vou fazer um preditor com ordem de 16
N = 16

rxx = calculate_autocorrelation(audio_data, N) # Vai de 0 a N - N+1 elementos

rxx_full = calculate_autocorrelation(audio_data, len(audio_data))
# Sxx = np.fft.fft(rxx_full)
# Sxx_log = 10 * np.log10(np.abs(Sxx))

N_samples = len(audio_data)

fft_values = np.fft.fft(audio_data)
power_spectrum = np.abs(fft_values) ** 2

psd = power_spectrum / N_samples

freqs = np.fft.fftfreq(N_samples, 1 / 44100)
positive_freqs = freqs[:N_samples // 2]
psd = psd[:N_samples // 2]

plt.figure()
plt.subplot(311)
plt.plot(rxx_full)
plt.subplot(312)
plt.plot(positive_freqs, psd)
plt.yscale('log')
plt.grid()
plt.subplot(313)
plt.psd(audio_data, NFFT=len(audio_data), Fs=44100)

plt.tight_layout()
plt.show()


