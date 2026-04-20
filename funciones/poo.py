class Persona:  # Clase Padre
    def __init__(self, nombre, id_):
        self.nombre = nombre
        self.id = id_

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")


class Empleado(Persona):  # Clase Hija (hereda de Persona)
    def __init__(self, nombre, id_, salario, cargo):
        # Llama al constructor de la clase padre
        super().__init__(nombre, id_)
        self.salario = salario
        self.cargo = cargo

    # Método específico de Empleado
    def trabajar(self):
        print(f"{self.nombre} está trabajando como {self.cargo}.")


# Uso
empleado1 = Empleado("Ana", "E101", 50000, "Gerente")
empleado1.saludar()  # Método heredado de Persona
empleado1.trabajar()  # Método propio de Empleado