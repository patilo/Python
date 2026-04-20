from main import *
from Color import *

class Rectangulo(FiguraGeometrica, Color):
        def __init__(self, alto, ancho, color):
                FiguraGeometrica.__init__(self, ancho, alto)
                Color.__init__(self, color)

        def Calcular_Area(self):
                return self.ancho * self.alto

        def __str__(self):
                return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'