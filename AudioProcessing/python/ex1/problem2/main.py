# from autocorrelation import compute_autocorrelation, plot_autocorrelation
from noise_generator import noise_generator, plot_iir
from prediction import predictor_YuleWalker
import matplotlib.pyplot as plt
from scipy.signal import welch
import numpy as np
import wave
from split_signal import split_signal

fig, axs = plt.subplots(4, 2)

# Open audio file and extract framerate + signal
with wave.open('../files_tut1/speech_sample.wav', 'rb') as wav_file:
    global signal
    global fs

    signal = wav_file.readframes(-1)
    signal = np.frombuffer(signal, dtype=np.int16)
    fs = wav_file.getframerate()
# fs = 44100
# signal = noise_generator(20000)
N = 12

len_blocks = 512 

welch_factor = 512

axs[0][0].plot(signal)
axs[0][0].set_title('Signal')

x_scale = range(10000, 10200)
axs[0][1].plot(x_scale, signal[x_scale])
axs[0][1].set_title('Zoom in signal')

singal_est, a = predictor_YuleWalker(signal, N)
error = signal - singal_est
axs[1][0].stem(a)
axs[1][0].set_title('Predictor Coefficients')

axs[1][1].plot(signal, label='Signal')
axs[1][1].plot(singal_est, label='Estimation')
axs[1][1].plot(error, label='Error')
axs[1][1].legend()
axs[1][1].set_title('Signal, estimation and error')

axs[2][0].psd(signal, NFFT=1024, Fs=fs, label='Signal')
axs[2][0].psd(error, NFFT=1024, Fs=fs, label='Error')
axs[2][0].set_title('PSD of signal and error')
axs[2][0].legend()


f, Pxx_signal = welch(signal, fs, nperseg=welch_factor, noverlap=welch_factor//2)
f, Pxx_error = welch(error, fs, nperseg=welch_factor, noverlap=welch_factor//2, window='hann')
axs[2][1].plot(f, 10*np.log10(Pxx_signal), label='Signal')
axs[2][1].plot(f, 10*np.log10(Pxx_error), label='Error')
axs[2][1].set_title('PSD of signal and error using Welch')
axs[2][1].legend()
axs[2][1].grid()

blocked_signal = split_signal(signal, len_blocks, 0.5, np.hanning(len_blocks))
blocked_prediction = [(predictor_YuleWalker(block, N)[0]) for block in blocked_signal]
blocked_error_matrix = [(predictor_YuleWalker(block, N)[0] - block) for block in blocked_signal]
blocked_error = np.concatenate(blocked_error_matrix)
# blocked_error_mean = np.mean(blocked_error_matrix, axis=0)
# print(blocked_signal[1].shape, blocked_prediction[1].shape)
# axs[3][0].plot(blocked_signal[12], label='Signal')
# axs[3][0].plot(blocked_prediction[12], label='Prediction', alpha=0.5)

axs[3][0].plot(signal[110000:111000], label='Signal')
axs[3][0].plot(blocked_error[110000:111000], label='Prediction', alpha=0.5)

axs[3][0].grid()
# axs[3][0].legend()
axs[3][0].set_title('Signal and error using blocked processing')

f, Pxx_signal = welch(signal, fs, nperseg=welch_factor, noverlap=welch_factor//2)
f, Pxx_error = welch(blocked_error, fs, nperseg=welch_factor, noverlap=welch_factor//2, window='hann')
axs[3][1].plot(f, 10*np.log10(Pxx_signal), label='Signal')
axs[3][1].plot(f, 10*np.log10(Pxx_error), label='Error')
axs[3][1].set_title('PSD of signal and error using Welch')
axs[3][1].legend()
axs[3][1].grid()

plt.tight_layout()
plt.show()