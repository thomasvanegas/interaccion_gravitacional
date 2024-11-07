class Punto2D:
    # Metodo constructor de la clase Punto2D
    def __init__(self, xi, yi):
        self.xi = xi
        self.yi = yi

    # Metodo getter y setter para la coordenada x
    def get_xi(self):
        return self.xi
    
    def set_xi(self, xi):
        self.xi = xi

    # Metodo getter y setter para la coordenada y
    def get_yi(self):
        return self.yi
    
    def set_yi(self, yi):
        self.yi = yi

    # Metodo para calcular la distancia entre dos puntos
    def calcular_distancia(self, punto: 'Punto2D'):
        return np.sqrt((punto.get_xi() - self.xi)**2 + (punto.get_yi() - self.yi)**2)
