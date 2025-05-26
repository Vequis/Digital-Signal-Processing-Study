import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.io.wavfile import write


def record_audio(duration=5, sample_rate=44100, name="output.wav", plot=False):
    """
    Records audio for a given duration and sample rate.

    Parameters:
    duration (int): Duration of the recording in seconds.
    sample_rate (int): Sample rate in Hz (samples per second).

    Returns:
    numpy.array: Recorded audio data.
    """
    print(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished!")

    audio_data_int16 = np.int16(audio_data * 32767)

    # Save to a WAV file
    write("output.wav", sample_rate, audio_data_int16)
    print("Audio saved as output.wav")

    
    if plot:    
        plt.figure()
        plt.plot(audio_data)
        plt.xlabel('Amostra')
        plt.ylabel('Amplitude')
        plt.show()

    return audio_data_int16

def load_audio_to_numpy(file_path):
    data, samplerate = sf.read(file_path)
    return np.array(data)

# audio_data = record_audio(5, 44100)
# print(len(audio_data))

