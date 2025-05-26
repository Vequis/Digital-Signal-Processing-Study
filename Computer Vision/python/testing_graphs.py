from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Gerar uma matriz de exemplo (10 linhas x 100 colunas)
matrix = np.random.rand(100, 100)

# Inicialmente, plottar a primeira linha da matriz
x = 0

vector=  np.random.rand(200)

# Criar a figura e o eixo do gráfico
fig, ax = plt.subplots()
line, = ax.plot(vector[0:100], lw=2)
ax.set_title(f"Linha {x}")

# Ajustar a posição do gráfico para abrir espaço para o slider
plt.subplots_adjust(bottom=0.25)

# Adicionar um slider abaixo do gráfico
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03])
line_slider = Slider(ax_slider, 'Linha', 0, 99, valinit=x, valstep=1)

# Função para atualizar a linha plottada
def update(val):
    global x
    x = (x + 1)%100
    line.set_ydata(vector[x: x + 100])
    ax.set_title(f"Linha {x}")
    fig.canvas.draw_idle()
    line_slider.set_val(x)

# Conectar a função de atualização ao slider
# line_slider.on_changed(update)

ani = FuncAnimation(fig, update, interval=20, save_count=100)

# Mostrar o gráfico
plt.show()
