import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

# Função de interpolação linear
def linear_interpolation(x, x1, y1, x2, y2):
    return y1 + (x - x1) * ((y2 - y1) / (x2 - x1))

# Frames originais
x_orig = [0, 1, 2, 3]
y_orig = [0, 1, 4, 9]

# Número de frames a adicionar entre cada par de frames originais
num_frames_to_add = 5

# Frames interpolados
x_interp = []
y_interp = []
for i in range(len(x_orig) - 1):
    x1, y1 = x_orig[i], y_orig[i]
    x2, y2 = x_orig[i+1], y_orig[i+1]
    for j in range(num_frames_to_add):
        x = x1 + (j+1) * (x2 - x1) / (num_frames_to_add + 1)
        y = linear_interpolation(x, x1, y1, x2, y2)
        x_interp.append(x)
        y_interp.append(y)

# Carregar as imagens
img1 = Image.open('imagem1.png')
img2 = Image.open('imagem2.png')

# Função de atualização dos frames na animação
def update_frame(frame):
    plt.clf()

    # Plot das imagens
    plt.imshow(img1, extent=[-1, 4, -1, 10])
    plt.imshow(img2, extent=[-1, 4, -1, 10], alpha=0.5)

    # Plot dos frames originais
    plt.plot(x_orig, y_orig, marker='o', color='b', label='Frames Originais')

    # Plot dos frames interpolados
    if frame is not None:
        x = x_interp[:frame+1]
        y = y_interp[:frame+1]
        plt.plot(x, y, marker='o', color='r', label='Frames Interpolados')

    # Diferença entre os frames originais e interpolados
    plt.plot(x_orig, y_orig, marker='o', linestyle='dashed', color='b', label='Diferença')
    plt.plot(x_interp[:frame+1], y_interp[:frame+1], marker='o', linestyle='dashed', color='r')

    # Legenda
    plt.legend()

# Configuração da animação
fig = plt.figure()
ani = animation.FuncAnimation(fig, update_frame, frames=len(x_interp), interval=500)

# Exibição da animação
plt.show()
