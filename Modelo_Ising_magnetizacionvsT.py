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
""""
# Condicion inicial con matriz de espines
s = np.random.choice([-1, 1], size=(N + 2, N + 2))
s = actualizarbordes(s)

"""
#Condición de que valga 1
s=np.ones((N + 2, N + 2))
s=actualizarbordes(s)


mag=[]
mag=np.array(mag)

magtemp=[]
magtemp=np.array(magtemp)

magerror=[]
magerror=np.array(magtemp)

temperaturas = np.arange(0.5, 5, 0.5)

for T in temperaturas: 
    for i in range(10000):
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

    magtemp=np.append(magtemp,np.mean(mag))
    magerror=np.append(magerror,np.std(mag))
    mag=np.zeros(0)

    

plt.errorbar(temperaturas, magtemp, yerr=magerror, fmt='-x', ecolor='red', label=f"Estado estacionario\nN={N}",capsize=5)
plt.xlabel('Temperatura')
plt.ylabel('Magnetización')
plt.title(f'Magnetización en función de T')
plt.legend()
plt.grid(True)
plt.savefig('Magnetización en función de la temperatura1.png')
plt.show()

