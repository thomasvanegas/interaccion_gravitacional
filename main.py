
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

# Definicion de constantes y variables globales
G = 6.67430e-11 # Constante de gravitacion universal
m = 5.972e24 # Masa de la Tierra en kg
Rt = 6371e3 # Radio de la Tierra en metros

# Definicion de la coordenada de la masa "m" fija
xi = 0
yi = 0

# Definicion del tamaño de la malla (100 x 100 puntos)
# Referencia: https://numpy.org/devdocs/reference/generated/numpy.linspace.html
tamano_malla = 100

x = np.linspace(-100, 100, tamano_malla)
y = np.linspace(-100, 100, tamano_malla)

# Creacion de la malla de puntos
# Referencia: https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-numpy
X, Y = np.meshgrid(x, y)

# Calcular la distancia entre la masa "m" fija y cada punto de la malla -> distancia entre dos puntos usando geometria analitica
distancia = np.sqrt((X - xi)**2 + (Y - yi)**2)

# Evitar la division por cero
distancia[distancia == 0] = 1e-10

# Calcular el potencial gravitacional (V) en cada punto de la malla
V = -G * m / distancia

# Graficar el potencial gravitacional (V)
fig, ax = plt.subplots(figsize=(8, 6))
cp = ax.contourf(X, Y, V, levels=50, cmap='inferno')
plt.colorbar(cp, label='Potencial Gravitacional (V)')
plt.title("Potencial Gravitacional V(x, y)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Posicion y masa de una masa m'
m_prima = 7.348e22 # Masa de la Luna en kg
x_prima = 20
y_prima = 20

# Calcular la distancia entre la masa fija Mt y la masa m'
distancia_m_prima = np.sqrt((x_prima - xi)**2 + (y_prima - yi)**2)

# Calcular la energia potencial gravitacional (U) de la sistema m - m'
U = (-G * m * m_prima) / distancia_m_prima

print(f"La energia potencial gravitacional del sistema m - m' es: {U} Joules")