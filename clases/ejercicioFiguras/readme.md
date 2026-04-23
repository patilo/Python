Estructura del Proyecto POO

figura.py: Clase base para definir la interfaz.
cuadrado.py: Clase específica que hereda de la base.
circulo.py: Clase específica que hereda de la base.
main.py: Archivo principal que importa las clases y las ejecuta.

Archivo figura.py (Clase Base)
Este archivo define la clase principal que será heredada, estableciendo la estructura básica y los métodos que las clases hijas deben implementar (polimorfismo).

Archivo cuadrado.py (Clase Hija)
Este archivo importa la clase base y define la lógica específica para la figura Cuadrado, demostrando Herencia y Polimorfismo.

Archivo circulo.py (Clase Hija)
Similar al cuadrado, este archivo define la lógica del círculo, que también hereda de Figura.

Archivo main.py (Ejecución Principal)
Este archivo es el punto de entrada del programa. Importa las clases y utiliza el Polimorfismo para manipular los objetos de forma genérica.