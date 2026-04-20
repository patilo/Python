import sys
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

criterio = int(sys.argv[1])
criterio2 = (sys.argv[2])
def filtrar(diccionario, precio):
    if criterio2 == "menor":
        crit_2 = {k for k, p in diccionario.items() if p<precio}
        print("los productos menores al umbral son: ")
    elif criterio2 == "mayor":
        crit_2 = {k for k, p in diccionario.items() if p>precio}
        print("los productos mayores al umbral son: ")
    elif criterio2 == "otro":
        crit_2 = {k for k, p in diccionario.items() if p>precio}
        print("no hay otro")
    else:
        print("lo sentimos, no es una operacion valida")
    (exit)
    return crit_2
print(filtrar(precios, criterio))