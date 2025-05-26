import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def noise_generator(N):
    """
    Generates N samples of almost pink noise by filtering a white noise process
    """
    w_white = np.random.randn(N)
    b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
    a = [1, -2.494956002, 2.017265875, -0.522189400]
    w = signal.lfilter(b, a, w_white)
    return w



def plot_iir(ax):
    b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
    a = [1, -2.494956002, 2.017265875, -0.522189400]
    w, h = signal.freqz(b, a)

    print(w)
    ax.plot(w, 20 * np.log10(abs(h)))
    ax.set_title('IIR filter frequency response')
    ax.set_xlabel('Frequency [radians / sample]')
    ax.set_ylabel('Amplitude [dB]')
    ax.grid()