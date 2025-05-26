import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 2*np.pi, 1000)
x = np.sin(t)
x = x + np.random.normal(0, 0.1, len(x))

X = np.fft.fft(x)
X = np.abs(X)

impulse_train = np.zeros(1000)
impulse_train[::10] = 1

xc = x * impulse_train

plt.figure()
plt.subplot(221)
plt.plot(t, x)
plt.subplot(222)
plt.plot(X)
plt.subplot(223)
plt.plot(xc)
plt.subplot(224)
plt.plot(np.abs(np.fft.fft(xc)))
plt.show()