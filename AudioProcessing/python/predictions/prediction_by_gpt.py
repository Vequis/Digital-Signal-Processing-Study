import numpy as np
import time
import matplotlib.pyplot as plt


N=10
def compute_autocorrelation(signal, print_time=False):
    """
    Compute the autocorrelation vector for k = 0, 1, ..., N.
    """
    start_time = time.time()

    n = len(signal)
    print('n:', n, " ;N:", N)
    rxx = np.zeros(N + 1)
    for lag in range(N + 1):
        x = signal[:n - lag] * signal[lag:]
        rxx[lag] = np.sum(x)
        rxx[lag] /= len(x)

    end_time = time.time()
    if print_time:
        print(f"Execution time: {end_time - start_time} seconds")
    return rxx

# compute_autocorrelation using np.correlate
def compute_autocorrelation_np(signal, print_time=False):
    # Aparentemente, essa função é MUITO mais lenta que a anterior
    start_time = time.time()
    
    N_samples = len(signal)
    result = np.correlate(signal, signal, mode='full')[N_samples-1:N_samples+N] / np.arange(N_samples, N_samples - N - 1, -1)
    
    end_time = time.time()
    if print_time:
        print(f"Execution time with np.corr: {end_time - start_time} seconds")
    
    return result


# def compute_autocorrelation(signal, aaa):
#     autocorrelation = np.zeros(N+1)
#     for k in range(N+1):
#         for n in range(N):
#             autocorrelation[k] += signal[n] * signal[(n + k)%N]
#         autocorrelation[k] /= (N)
#     return autocorrelation

def compute_prediction_coefficients(signal, N):
    """
    Compute the optimal prediction coefficients for a signal using Yule-Walker equations.
    """
    # Step 1: Compute the autocorrelation vector up to lag N
    rxx = compute_autocorrelation(signal, N)

    # Step 2: Construct the autocorrelation matrix Rxx (Toeplitz matrix)
    Rxx = np.array([[rxx[np.abs(i - j)] for j in range(N)] for i in range(N)])
    rxx_1 = rxx[1:N+1]

    # Step 3: Solve for a_opt using pseudo-inverse or least squares
    a_opt = np.linalg.pinv(Rxx) @ rxx_1

    return a_opt

def predict_signal(signal):
    """
    Predict the signal using the prediction coefficients.
    """

    a_opt = compute_prediction_coefficients(signal, N)
    predicted_signal = np.zeros(len(signal))
    for n in range(N, len(signal)):
        # Predict x(n) using the past N values and coefficients
        predicted_signal[n] = np.sum(a_opt * signal[n - np.arange(1, N+1)])
    return predicted_signal

# Example usage:


def example_case():
    N_samples = 200
    t = np.linspace(0, 0.001 * N_samples, N_samples, endpoint=False)
    sinal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
    sinal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
    ruido = np.random.normal(0, 0.1, N_samples)  # Ruído gaussiano branco com média 0 e desvio padrão 0.1
    sinal_com_ruido = sinal + ruido
    signal = sinal_com_ruido
    signal = sinal

    # Compute the prediction coefficients
    a_opt = compute_prediction_coefficients(signal, N)
    # print("Prediction Coefficients (a_opt):", a_opt)

    # Predict the signal
    predicted_signal = predict_signal(signal)
    # print("Predicted Signal:", predicted_signal)

    error = np.abs(signal - predicted_signal)
    print("Mean Absolute Error:", np.mean(error[N:]))

    plt.figure()
    plt.plot(signal, label='Original Signal')
    plt.plot(predicted_signal, label='Predicted Signal')
    plt.plot(error, label='Prediction Error', linestyle='--', color='red')
    plt.legend()
    plt.show()

def testing_correlations():
    # Código porco
    N_samples = 20000
    t = np.linspace(0, 0.001 * N_samples, N_samples, endpoint=False)
    sinal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
    sinal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
    ruido = np.random.normal(0, 0.1, N_samples)  # Ruído gaussiano branco com média 0 e desvio padrão 0.1
    sinal_com_ruido = sinal + ruido
    signal = sinal_com_ruido
    signal = sinal

    ac = compute_autocorrelation(signal, print_time=True)
    ac_np = compute_autocorrelation_np(signal, print_time=True)

    plt.figure()
    plt.subplot(211)
    plt.plot(ac)
    plt.subplot(212)
    plt.plot(ac_np)
    plt.show()

# testing_correlations()
example_case()



