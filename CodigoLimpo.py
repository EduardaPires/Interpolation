import matplotlib.pyplot as plt # para criação dos gráficos
import matplotlib.animation as animation # para animação
import numpy as np #para a criação de matrizes

# Função de interpolação linear
def linear_interpolation(x1, y1, x2, y2):
    # x = x1 + (j+1) * (x2 - x1) / (framesToAdd + 1)
    matrixA = np.array([[x1, 1], [x2, 1]]) 
    results = np.array([y1, y2])
    solution = np.linalg.solve(matrixA, results)
    a = solution[0]
    b = solution[1]
    return x, a*x+b
  
framesX = [2, 4, 6, 8, 10]
secondsY = [1, 2, 3, 4, 5] 
framesToAdd = 5
newFramesX = [] 
newIntSecondsY = [] 


for i in range(len(framesX) - 1): 
    x1, y1 = framesX[i], secondsY[i] 
    x2, y2 = framesX[i+1], secondsY[i+1]
    for j in range(framesToAdd):
        x = x1 + (j+1) * (x2 - x1) / (framesToAdd + 1)
        y = linear_interpolation(x1, y1, x2, y2)
        newFramesX.append(x)
        newIntSecondsY.append(y)


def update_frame(newValue): 
    plt.clf() 
    plt.plot(framesX, secondsY, marker='o', color='b', label='Frames Originais')
    x = newFramesX[:newValue+1] 
    y = newIntSecondsY[:newValue+1]
    plt.plot(x, y, marker='o', color='r', label='Frames Interpolados')
    plt.legend() 

fig = plt.figure()
ani = animation.FuncAnimation(fig, update_frame, frames=len(newFramesX), interval=500) 
plt.show()
