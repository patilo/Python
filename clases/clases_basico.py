class Animal:
    # Propiedad de la clase (común a todas las instancias)
    especie = "Mamífero"

    # Constructor (método especial, ver punto 2)
    def __init__(self, nombre, edad):
        # Propiedades de la instancia (atributos)
        self.nombre = nombre
        self.edad = edad

    # Método (comportamiento)
    def hacer_sonido(self):
        print(f"{self.nombre} está haciendo un sonido.")


# Creación de objetos (instanciación)
mi_perro = Animal("Fido", 5)
mi_gato = Animal("Miau", 3)

# Acceder a propiedades
print(f"El perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} años.")
print(f"La especie del gato es {mi_gato.especie}.")

# Llamar a un método
mi_perro.hacer_sonido()