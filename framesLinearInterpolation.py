import matplotlib.pyplot as plt # para criação dos gráficos
import matplotlib.animation as animation # para animação
import numpy as np #para a criação de matrizes

# Função de interpolação linear
def linear_interpolation(x1, y1, x2, y2):
    
    # definição do x que será inserido entre os pontos; no caso de framesToAdd for 1 por exemplo, ele será exatamente o ponto central entre x1 e x2
    x = x1 + (j+1) * (x2 - x1) / (framesToAdd + 1)
    
    # matriz para achar os coeficientes: 
    matrixA = np.array([[x1, 1], [x2, 1]]) #pois essa matriz multiplicada pelos coeficientes resultará em y, ex: a * x1 + b * 1 = y1

    # matriz com os resultados (y):
    results = np.array([y1, y2])

    # função para resolver o sistema 
    solution = np.linalg.solve(matrixA, results)

    # pegar os valores encontrados dos coeficientes:
    a = solution[0]
    b = solution[1]
    return x, a*x+b

    # coefA= (y2 - y1) / (x2 - x1) #formula para achar o A da equação
    # coefB = y1 - coefA*x1 #formula para achar o B
    # return coefA*x + coefB
    # #return y1 + (x - x1) * ((y2 - y1) / (x2 - x1))


# dataset constante de 2fps --> y=0,5x
framesX = [2, 4, 6, 8, 10]
secondsY = [1, 2, 3, 4, 5] 

# Número de frames a adicionar entre cada par de frames originais (x1 e x2)
framesToAdd = 5

# Frames interpolados
newFramesX = [] #declaração do array que conterá os novos frames
newIntSecondsY = [] #declaração do array com o novos ys, nesse caso representaria os novos intervalos de tempo entre os quadros
for i in range(len(framesX) - 1): # irá percorrer o array dos pontos de x (frames) originais
    x1, y1 = framesX[i], secondsY[i] # declaração dos pares de pontos x1,y1
    x2, y2 = framesX[i+1], secondsY[i+1] #x2,y2 são os pontos localizados logo após, portanto já estão na próxima posição do array
    for j in range(framesToAdd): #loop que acontece a quantidade de vezes em que queremos adicionar um novo frame no intervalo x1 e x2; se só quisermos adicionar um frame, só ocorrerá uma vez
        x,y = linear_interpolation(x1, y1, x2, y2)
        newFramesX.append(x)
        newIntSecondsY.append(y)

# Para a animação dos pontos novos no gráfico:
def update_frame(newValue): #método update é chamado a todo momento, a cada quadro fornecido
    plt.clf() #função responsável por limpar o quadro atual para que o próximo tome seu lugar; nesse caso é apenas para as legendas não se replicarem

    # Gráfico dos frames originais
    plt.plot(framesX, secondsY, marker='o', color='b', label='Frames Originais')

    # Adição dos frames interpolados
    x = newFramesX[:newValue+1] #criação de sublistas com os valores de newFrames e newSeconds para que armazene e mostre gradualmente cada ponto adicionado/interpolado
    y = newIntSecondsY[:newValue+1]
    plt.plot(x, y, marker='o', color='r', label='Frames Interpolados')

    plt.legend() #para colocar as legendas

fig = plt.figure() #criação da figura com o gráfico
ani = animation.FuncAnimation(fig, update_frame, frames=len(newFramesX), interval=500) #fução para criar a animação; como parametros temos: a figura, a função de update, quadros da animação, que atualiza a cada ponto interpolado, e interval que é a velocidade 

# Exibição do gráfico
plt.show()
