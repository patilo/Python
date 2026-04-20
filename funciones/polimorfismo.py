class Perro(Animal): # Hereda de Animal (del ejemplo inicial)
    def hacer_sonido(self): # Sobrescribe el método de Animal
        print(f"{self.nombre} dice: ¡Guau! 🐶")

class Gato(Animal): # Hereda de Animal
    def hacer_sonido(self): # Sobrescribe el método de Animal
        print(f"{self.nombre} dice: ¡Miau! 🐱")

# Uso polimórfico
perro = Perro("Toby", 4)
gato = Gato("Luna", 2)

# Se llama al mismo método 'hacer_sonido', pero el comportamiento es diferente
perro.hacer_sonido()
gato.hacer_sonido()

# Función que toma cualquier objeto que tenga el método hacer_sonido
def probar_sonido(animal):
    animal.hacer_sonido()

probar_sonido(perro)
probar_sonido(gato)