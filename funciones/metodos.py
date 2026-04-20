def arrancar(self):
    if not self.encendido:
        self.encendido = True
        print(f"El {self.modelo} ha arrancado.")
    else:
        print(f"El {self.modelo} ya está encendido.")

# Uso
mi_coche = Coche("Toyota", "Corolla", 2020)
mi_coche.arrancar()


def saludar(nombre):
    """Esta función imprime un saludo con el nombre dado."""
    print(f"¡Hola, {nombre}! Bienvenido a Python.")

# Llamada a la función
saludar("Andrea")
saludar("Carlos")


def restar(a, b): # 'a' y 'b' son PARÁMETROS
    return a - b

# 10 y 4 son ARGUMENTOS
resultado = restar(10, 4)
print(resultado) # Salida: 6



def calcular_iva(precio, tasa=0.19):
    impuesto = precio * tasa
    return impuesto # Devuelve el valor del impuesto

precio_producto = 100
iva_calculado = calcular_iva(precio_producto)

print(f"El IVA es: {iva_calculado}") # Salida: El IVA es: 19.0