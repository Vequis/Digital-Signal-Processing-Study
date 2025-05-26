from autocorrelation import compute_autocorrelation
import numpy as np

def calculate_parameters(x, N):
    rxx = compute_autocorrelation(x, N) # Goes from 0 to N

    Rxx = np.array([[rxx[abs(i - j)] for j in range(N)] for i in range(N)])

    rxx_1 = rxx[1:]
    return np.linalg.solve(Rxx, rxx_1)

def predictor_YuleWalker(x, N):
    a = calculate_parameters(x, N)

    x_estimation = np.zeros_like(x)
    x_estimation[:N] = x[:N]
    x_estimation[N-1:] = np.convolve(a, x, mode='valid')

    return x_estimation, a





