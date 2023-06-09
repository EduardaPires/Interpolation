import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

# Função de interpolação linear
def linear_interpolation(j, x1, y1, x2, y2):
    #x = x1 + (j+1) * (x2 - x1) / (num_frames_to_add  + 1)
    return y1 + (x - x1) * ((y2 - y1) / (x2 - x1))

# Frames originais (imagens)
image1 = Image.open("1.png") #seria o primeiro x,y
image2 = Image.open("2.png") #x2,y2
image3 = Image.open("3.png") #x3, y3


# Número de frames a adicionar entre cada par de frames originais
num_frames_to_add = 10


# Frames interpolados
interp_images = []
for i in range(num_frames_to_add):
    t = (i + 1) / (num_frames_to_add + 1)
    #t = linear_interpolation(j, )
    interp_image = Image.blend(image1, image2, t)
    interp_image2 = Image.blend(image2, image3, t)
    interp_image3 = Image.blend(image3, image2, t)
    interp_image4 = Image.blend(image2, image1, t)
    interp_images.append(interp_image)
    interp_images.append(interp_image2)
    interp_images.append(interp_image3)
    interp_images.append(interp_image4)

# Função de atualização dos frames na animação
def update_frame(frame):
    plt.clf()

    # Plot da imagem original
    plt.imshow(image1)

    # Plot das imagens interpoladas
    if frame is not None:
        for i in range(frame + 1):
            plt.imshow(interp_images[i], alpha=0.9)

    # Configurações de plotagem
    plt.axis('off')

# Configuração da animação
fig = plt.figure()
ani = animation.FuncAnimation(fig, update_frame, frames=len(interp_images), interval=200)

# Exibição da animaçãoimage.png
plt.show()