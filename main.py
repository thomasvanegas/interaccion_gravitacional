
"""
@author: Thomas Camilo Vanegas Acevedo
@date: 2024-NOV-08
@description: Este script calcula el potencial gravitacional y la energia potencial gravitacional de un sistema para dos masas.
ID: 000287437

Un cuerpo de masa m se encuentra ubicado en el plano en la coordenada O(Xi, Yi).

a. Calcular el potencial gravitacional (V) que este cuerpo genera en cualquier punto P(x, y) alrededor del punto O
para esto cree una malla de 100 x 100 puntos.

b. Graficar el potencial gravitacional (V) en el plano XY.

c. Si se coloca una masa m' en una posicion dentro de la malla de puntos, y deja la masa m fija en el punto O,
calcular la energia potencial gravitacional (U) del sistema m - m'.

"""

"""
Definiciones y conceptos para el desarrollo del script

Fuerza de gravitacion: F = (-G * m1 * m2) / r^2

Potencial gravitacional: V = (-G * m1) / r

Energia potencial gravitacional: U = (-G * m1 * m2) / r

Campo gravitacional: g = F / m2 = (-G * m1) / r^2
"""

# Importacion de librerias, modulos y clases
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Punto2D import Punto2D

# Definicion de constantes y variables globales
G = 6.67430e-11 # Constante de gravitacion universal
m = 5.972e24 # Masa de la Tierra en kg
m_prima = 1000   # Masa de la partícula m' en kg

# Definicion de funciones para calcular el potencial gravitacional y la energia potencial gravitacional
def calcular_potencial_gravitacional(m, punto_o: 'Punto2D', punto: 'Punto2D'):
    distancia = punto.calcular_distancia(punto_o)
    if distancia == 0:
        return np.inf  # Evitar división por cero en el punto de la masa
    return (-G * m) / distancia

def calcular_energia_potencial_gravitacional(m, m_prima, punto_o: Punto2D, punto: Punto2D):
    distancia = punto.calcular_distancia(punto_o)
    if distancia == 0:
        raise ValueError("La distancia entre las masas no puede ser cero (están en la misma posición).")
    return (-G * m * m_prima) / distancia

# Definicion del tamaño de la malla (100 x 100 puntos)
# Referencia: https://numpy.org/devdocs/reference/generated/numpy.linspace.html
# Generar una malla de 100x100 puntos alrededor del origen (0, 0)
x_values = np.linspace(-100, 100, 100)
y_values = np.linspace(-100, 100, 100)


# Creacion de la malla de puntos
# Referencia: https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-numpy
X, Y = np.meshgrid(x_values, y_values)

# Instanciamiento de la coordenada de la masa "m" fija
punto_o = Punto2D(0, 0)

# Calcular el potencial gravitacional en cada punto de la malla
V = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        punto = Punto2D(X[i, j], Y[i, j])
        V[i, j] = calcular_potencial_gravitacional(m, punto_o, punto)

# Graficar el potencial gravitacional en 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear la gráfica de superficie
surf = ax.plot_surface(X, Y, V, cmap='viridis', edgecolor='none')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('Potencial Gravitacional (J/kg)')
ax.set_title('Potencial Gravitacional en 3D generado por una masa en el origen')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Potencial Gravitacional (J/kg)')

plt.show()

# Calcular la energía potencial gravitacional entre el sistema m-m'
# Coordenadas de la masa m' en un punto específico (por ejemplo, x'=1e7, y'=2e7 metros)
punto_m_prima = Punto2D(100, 100)

# Calcular la energía potencial gravitacional entre m y m'
U = calcular_energia_potencial_gravitacional(m, m_prima, punto_o, punto_m_prima)

print(f"Energía Potencial Gravitacional entre m y m' en el punto ({punto_m_prima.x}, {punto_m_prima.y}): {U:.2e} J")