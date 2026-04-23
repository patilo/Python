# cuadrado.py

# Importamos la clase Figura para heredar sus propiedades
from figura import Figura

class Cuadrado(Figura):
    """Clase para un Cuadrado que hereda de Figura."""
    def __init__(self, lado):
        # Llama al constructor de la clase padre (Figura)
        super().__init__("Cuadrado")
        self.lado = lado # Atributo específico del Cuadrado

    # Polimorfismo: Sobrescribimos el método del padre para el cálculo específico
    def calcular_area(self):
        return self.lado ** 2

    # Polimorfismo: Sobrescribimos el método del padre
    def calcular_perimetro(self):
        return 4 * self.lado