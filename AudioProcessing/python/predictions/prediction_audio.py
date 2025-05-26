import numpy as np
import matplotlib.pyplot as plt
from record_audio import load_audio_to_numpy
from prediction_by_gpt import predict_signal

audio_data = load_audio_to_numpy('e.wav')
audio_data = audio_data[85000:85200]  
predicted_signal = predict_signal(audio_data)
error = np.abs(audio_data - predicted_signal)

print("Erro médio:", np.mean(error))

plt.figure()
plt.plot(audio_data, label='Original')
plt.plot(predicted_signal, label='Predicted')
plt.xlabel('Amostra')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
