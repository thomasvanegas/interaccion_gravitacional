# Importacion de librerias, modulos y clases
import numpy as np

class Punto2D:
    # Metodo constructor de la clase Punto2D
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Metodo getter y setter para la coordenada x
    def get_x(self):
        return self.x
    
    def set_x(self, x):
        self.x = x

    # Metodo getter y setter para la coordenada y
    def get_y(self):
        return self.y
    
    def set_y(self, y):
        self.y = y

    def calcular_distancia(self, otro_punto):
        return np.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)    
