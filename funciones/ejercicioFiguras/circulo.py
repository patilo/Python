# circulo.py

import math
# Importamos la clase Figura para heredar sus propiedades
from figura import Figura

class Circulo(Figura):
    """Clase para un Círculo que hereda de Figura."""
    def __init__(self, radio):
        # Llama al constructor de la clase padre (Figura)
        super().__init__("Círculo")
        self.radio = radio # Atributo específico del Círculo

    # Polimorfismo: Sobrescribimos el método del padre
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    # Polimorfismo: Sobrescribimos el método del padre
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio