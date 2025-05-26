from predictions.record_audio import load_audio_to_numpy
from predictions.prediction_by_gpt import predict_signal
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Esse código é uma bagunça, mas é só pra testar a manipulação de sinais de áudio

audio_data = load_audio_to_numpy('e.wav')
audio_data = audio_data[80000:120000]
# Perform FFT and get magnitude and phase
X = np.abs(np.fft.fft(audio_data))
phase = np.angle(np.fft.fft(audio_data))

amount_of_components = 80

# Find the indices of the 3 components with the greatest magnitude
indices = np.argsort(X)[::-1][:amount_of_components]

# Create a new FFT array with only the 3 largest components
X_reduced = np.zeros_like(X)
X_reduced[indices] = X[indices] * np.exp(1j * phase[indices])

print(X_reduced)

# Perform the inverse FFT to reconstruct the signal
reconstructed_signal = np.fft.ifft(X_reduced).real

# Play the audio data with a sample rate of 44.1 kHz
# sd.play(audio_data, samplerate=44100)
# sd.wait()  # Wait until the audio is finished playing
sd.play(reconstructed_signal, samplerate=44100)
sd.wait()  # Wait until the audio is finished playing


# Plot the original and reconstructed signals for comparison
plt.figure()
plt.subplot(211)
plt.title('Original Signal')
plt.plot(audio_data)
plt.subplot(212)
plt.title(f'Reconstructed Signal with {amount_of_components} Largest Components')
plt.plot(reconstructed_signal)
plt.tight_layout()
plt.show()



# plt.figure()
# plt.subplot(311)
# plt.plot(np.abs(np.fft.fft(audio_data[84000:105000])))
# plt.subplot(312)
# plt.plot(np.abs(np.fft.fft(audio_data[85000:86000])))
# plt.subplot(313)
# plt.plot(np.abs(np.fft.fft(audio_data[86000:87000])))
# plt.show()
