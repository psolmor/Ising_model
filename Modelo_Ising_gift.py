import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random

def p(m, n, T, s):
    probabilidad = min(1, np.exp(-cambio_H(m, n, s) / T))
    return probabilidad

def cambio_H(m, n, s):
    delta_E = 2 * s[m, n] * (s[m - 1, n] + s[m + 1, n] + s[m, n + 1] + s[m, n - 1])
    return delta_E

def actualizarbordes(s):
    s[0, :] = s[-2, :]
    s[:, 0] = s[:, -2]
    s[-1, :] = s[1, :]
    s[:, -1] = s[:, 1]
    return s

N = 10
T = 1.5

# Condicion inicial con matriz de espines

#Condición de valores random
s = np.random.choice([-1, 1], size=(N + 2, N + 2))
s = actualizarbordes(s)

"""
#Condición de que valga 1
s=np.ones((N + 2, N + 2))
s=actualizarbordes(s)
"""

fig, ax = plt.subplots()
def update(frame):
    global s
    
    for i in range(N*N):

        m = random.randint(1, N)
        n = random.randint(1, N)

        probabilidad = p(m, n, T, s)
        u = random.random()

        if probabilidad > u:
            s[m, n] = -s[m, n] 
            s = actualizarbordes(s)

    mag_iteracion = np.mean(s[1:-1, 1:-1])
    mag=np.append(mag,mag_iteracion)
    
    ax.clear()
    ax.imshow(s[1:N+1,1:N+1], cmap='coolwarm', interpolation='nearest')
    ax.set_title(f'Configuración spin (Frame {frame})  magnetización={mag}  Temperatura={T}')
    
    return ax


#Cada iteración arriba me genera un paso montecarlo, con frames elijo en número de pasos montecarlo
frames = 1000


ani = animation.FuncAnimation(fig, update, frames=frames, interval=200, blit=False)
ani.save('ising_simulation.gif', writer='pillow', fps=10)
plt.show()

