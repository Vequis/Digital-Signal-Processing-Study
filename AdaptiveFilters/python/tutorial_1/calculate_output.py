import numpy as np
import matplotlib.pyplot as plt

def calculate_output(S_hat, size_y, N_fft=256, frameshift=64):
    """
    CALCULATE_OUTPUT Calculate the output of the Wiener filter
    
    Parameters:
    S_hat       -- Spectrogram (complex-valued STFT output) of the Wiener filter
    size_y      -- Length of the original noisy signal (used to size the output)
    N_fft       -- FFT resolution (optional, default=256)
    frameshift  -- Hop size in samples between frames (optional, default=64)

    Returns:
    s_hat       -- Time-domain output of the Wiener filter
    """
    
    N_f, N_t = S_hat.shape

    # Initialize the output signal with zeros
    s_hat = np.zeros(size_y)

    print('AAA')
    return

    # Convert each frame back to time domain and perform overlap-add
    for k in range(N_t):
        # Mirror and conjugate for real IFFT
        spectrum = np.concatenate([
            S_hat[:, k],
            np.conj(S_hat[-2:0:-1, k])
        ])

        print(k)
        print(S_hat[:, k])
        print(np.conj(S_hat[-2:0:-1, k]))

        # IFFT and scaling
        frame = np.real(np.fft.ifft(spectrum)) * frameshift / (N_fft / 2)

        # Overlap-add to the output signal
        start = k * frameshift
        end = start + N_fft

        if end <= size_y:
            s_hat[start:end] += frame
        else:
            s_hat[start:size_y] += frame[:size_y - start]

    return s_hat