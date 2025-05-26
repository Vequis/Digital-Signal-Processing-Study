import numpy as np
import matplotlib.pyplot as plt

N = 20
x = np.ones(N)
noise = np.random.normal(0, 0.1, N)
x = x + noise

tamanho_media_movel = 4
h = np.ones(tamanho_media_movel)
h /= np.sum(h)

def plot_x_h_conv(x, h):
    conv = np.convolve(x, h)
    plt.figure()
    plt.subplot(311)
    plt.stem(x, 'o-')
    plt.subplot(312)
    plt.stem(h, 'o-')
    plt.subplot(313)
    plt.stem(conv, 'o-')

    for ax in plt.gcf().get_axes():
        ax.set_xlim(-1, len(conv))

    plt.tight_layout()
    plt.show()

def media_movel(x, tamanho_media_movel):
    '''
    Calcula média movel e retorna o vetor da convolução
    '''
    h = np.ones(tamanho_media_movel)
    h /= np.sum(h)
    return np.convolve(x, h)

def plot_media_movel(x, tamanho_media_movel):
    h = np.ones(tamanho_media_movel)
    h /= np.sum(h)
    plot_x_h_conv(x, h)

# plot_x_h_conv(x, h)
plot_media_movel(x, 4)

