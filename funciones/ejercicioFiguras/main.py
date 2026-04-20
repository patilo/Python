# main.py

# Importamos las clases específicas
from cuadrado import Cuadrado
from circulo import Circulo
# También podemos importar la clase base si la necesitamos
from figura import Figura


def main():
    print("🚀 Iniciando Programa de Geometría POO (Modular)")
    print("---------------------------------------")

    # 1. Instanciación (Llamada a los Constructores)
    mi_cuadrado = Cuadrado(lado=6.0)
    mi_circulo = Circulo(radio=3.5)

    # 2. Demostración del Polimorfismo
    # Creamos una lista de objetos, sin importar de qué clase específica sean
    lista_figuras = [mi_cuadrado, mi_circulo]

    # Iteramos sobre la lista
    for figura in lista_figuras:
        # Llamamos al mismo método 'mostrar_info' para cada objeto.
        # El método internamente llama a la versión de 'calcular_area'
        # y 'calcular_perimetro' específica de cada figura (Cuadrado o Círculo).
        figura.mostrar_info()

    # Ejemplo adicional: una instancia de la clase base que fallará
    mi_figura_base = Figura("Figura Genérica Abstracta")
    mi_figura_base.mostrar_info()


# El bloque principal de ejecución
if __name__ == "__main__":
    main()