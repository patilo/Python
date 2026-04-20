def calcular_iva(precio, tasa=0.19):
    impuesto = precio * tasa
    return impuesto # Devuelve el valor del impuesto

precio_producto = 100
iva_calculado = calcular_iva(precio_producto)

print(f"El IVA es: {iva_calculado}") # Salida: El IVA es: 19.0

def potencia(base, exponente=2): # exponente tiene valor por defecto de 2
    return base ** exponente

print(potencia(3))       # Usa 2 como exponente. Salida: 9 (3^2)
print(potencia(3, 3))    # Sobrescribe el valor por defecto. Salida: 27 (3^3)