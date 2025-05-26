import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from matplotlib.animation import FuncAnimation

# Defina parâmetros
sample_rate = 44100  # Taxa de amostragem em Hz
duration = 10  # Duração da gravação em segundos
filename = "output.wav"  # Nome do arquivo de saída

# Criar uma figura para o gráfico
fig, ax = plt.subplots()
x = np.arange(0, int(sample_rate * 0.1))  # Eixo X para 0.1 segundos
line, = ax.plot(x, np.random.rand(int(sample_rate * 0.1)))
ax.set_ylim(-1, 1)
ax.set_xlim(0, len(x))

# Gravar áudio e plottar
print("Iniciando a gravação...")
with sf.SoundFile(filename, mode='w', samplerate=sample_rate, channels=1) as file:
    audio_data = np.empty((0, 1))

    def callback(indata, frames, time, status):
        if status:
            print(status)
        file.write(indata)  # Escrever os dados de áudio no arquivo
        global audio_data
        audio_data = np.vstack((audio_data, indata))  # Atualizar os dados de áudio

    def update_plot(frame):
        line.set_data(np.arange(len(audio_data)), audio_data[:, 0])  # Atualizar o gráfico com os novos dados de áudio
        ax.set_xlim(0, len(audio_data))  # Atualizar o limite do eixo X
        return line,

    ani = FuncAnimation(fig, update_plot, blit=True)

    with sd.InputStream(samplerate=sample_rate, channels=1, callback=callback):
        plt.show(block=True)
        sd.sleep(int(duration * 1000))  #s Dormir pelo tempo de gravação

print("Gravação finalizada e salva em", filename)
