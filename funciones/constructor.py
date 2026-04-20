class Coche:
    def __init__(self, marca, modelo, anio):
        # Inicializa los atributos de la instancia
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False # Atributo predeterminado


class Perro:
    # EL CONSTRUCTOR: Se llama al crear un objeto Perro
    def __init__(self, nombre_parametro, edad_parametro):
        # Inicializa los atributos de la instancia (self)
        self.nombre = nombre_parametro
        self.edad = edad_parametro

# Creación del Objeto (aquí se llama automáticamente a def __init__)
mi_perro = Perro("Fido", 5)

print(mi_perro.nombre) # Salida: Fido
print(mi_perro.edad)   # Salida: 5