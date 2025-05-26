import numpy as np

def quantize_signal(x, bits):
    x_ = np.copy(x)
    bits_array = np.zeros_like(x)
    signal_range = np.max(x) - np.min(x)
    step = signal_range / 2**bits
    half_step = step / 2

    minimo = np.min(x)

    N = int(len(x))
    for i in range(N):
        bits_array[i] = min((x[i] - minimo) // step, 2**bits - 1)
        x_[i] = bits_array[i] * step + np.min(x) + half_step


    return x_, bits
