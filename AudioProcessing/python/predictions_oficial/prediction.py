from autocorrelation import compute_autocorrelation
import numpy as np
import matplotlib.pyplot as plt

def compute_prediction_coefficients(signal, N):
    rxx = compute_autocorrelation(signal, N)

    Rxx = np.array([[rxx[np.abs(i - j)] for j in range(N)] for i in range(N)])
    rxx_1 = rxx[1:N+1]

    a_opt = np.linalg.solve(Rxx, rxx_1)

    return a_opt

def compute_prediction_error_gain(signal, N):
    # PREDICTION ERROR GAIN
    # Está diretamente relacionado com o quão mais "branco" é a DEP do erro
    
    # a_opt = compute_prediction_coefficients(signal, N)
    # rxx = compute_autocorrelation(signal, N)
    # rxx_1 = rxx[1:N+1]
    # Emin = rxx[0] - np.dot(rxx_1, a_opt)
    # return rxx[0] / Emin

    return np.var(signal) / np.var(signal - predict_signal(signal, N))


def predict_signal(signal, N):
    n = len(signal)
    predicted_signal = np.zeros(n)
    a_opt = compute_prediction_coefficients(signal, N)
    for i in range(N, n):
        predicted_signal[i] = np.sum(a_opt * signal[i - np.arange(1, N+1)])

    return predicted_signal

def plot_prediction_and_error(signal, N):
    prediction = predict_signal(signal, N)
    error = signal - prediction

    plt.figure()
    plt.plot(signal, label='Original Signal')
    plt.plot(prediction, label='Predicted Signal')
    plt.plot(error, label='Error Signal', linestyle='--', alpha=0.7, color='red')
    plt.legend()
    plt.grid()
    plt.show()

def plot_prediction_and_error_custom_ax(signal, N, ax):
    prediction = predict_signal(signal, N)
    error = signal - prediction

    ax.plot(signal, label='Original Signal')
    ax.plot(prediction, label='Predicted Signal')
    ax.plot(error, label='Error Signal', linestyle='--', alpha=0.7, color='red')
    ax.title.set_text(f'Prediction order = {N}')
    ax.legend()
    ax.grid()