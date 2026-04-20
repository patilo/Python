# Variable GLOBAL (accesible en todas partes)
x = 50

def mi_funcion():
    # Variable LOCAL (solo existe dentro de mi_funcion)
    x = 10
    print(f"Dentro de la función, x es: {x}") # Salida: 10

mi_funcion()
print(f"Fuera de la función, x es: {x}")  # Salida: 50