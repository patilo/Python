# figura.py

class Figura:
    """Clase base que define la interfaz común para todas las figuras."""

    def __init__(self, nombre):
        # Atributo de la clase base, inicializado por el constructor
        self.nombre = nombre

    def calcular_area(self):
        """Método que debe ser sobrescrito por las subclases (abstracto)."""
        raise NotImplementedError("La subclase debe implementar el método 'calcular_area'")

    def calcular_perimetro(self):
        """Método que debe ser sobrescrito por las subclases (abstracto)."""
        raise NotImplementedError("La subclase debe implementar el método 'calcular_perimetro'")

    def mostrar_info(self):
        """Método común para mostrar resultados."""
        print(f"\n--- {self.nombre} ---")
        try:
            print(f"Área: {self.calcular_area():.2f}")
            print(f"Perímetro: {self.calcular_perimetro():.2f}")
        except NotImplementedError as e:
            print(f"Error en la implementación: {e}")