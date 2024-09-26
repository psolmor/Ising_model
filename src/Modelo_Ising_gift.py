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
s = np.random.choice([-1, 1], size=(N + 2, N + 2))
s = actualizarbordes(s)

# Actualizar los bordes de la matriz de espines
s = actualizarbordes(s)

# Inicializar la variable mag
mag = np.array([])

# Función para actualizar la matriz de espines
def actualizar_espines(s, T):
    for _ in range(N * N):
        m = random.randint(1, N)
        n = random.randint(1, N)
        if random.random() < p(m, n, T, s):
            s[m, n] *= -1
    s = actualizarbordes(s)
    return s

# Configuración de la animación
fig, ax = plt.subplots()
im = ax.imshow(s, cmap='coolwarm', interpolation='nearest')

def update(frame):
    global s, mag
    s = actualizar_espines(s, T)
    im.set_array(s)
    
    # Calcular la magnetización
    mag_iteracion = np.sum(s)
    mag = np.append(mag, mag_iteracion)
    
    return [im]

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Guardar la animación como un archivo GIF
ani.save('ising_simulation.gif', writer='pillow', fps=10)

plt.show()

