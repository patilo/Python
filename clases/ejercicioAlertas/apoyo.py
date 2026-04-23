#Definimos el Lactorial
def factorial(numero):
    fact = 1  #Inicializamos el factorial el 1
    for i in range(numero):  #Iteramos para cada numero anterior al numero entregrado
        fact *= i+1   #Calculamos el factorial multiplicando el resultado anterior con el presente
    print(f'El factorial de {numero} es {fact}') #Imprimo resultado

#Definimos la Productoria
def pitatoria(lista):
    pita = 1  #Inicializamos la productoria en 1
    for num in lista:  #Iteramos sobre los elementos de la lista
        pita *= num   #Calculamos el producto entre los elementos de la lista
    print(f'La productoria de {lista} es {pita}') #Imprimo resultado

#Definimos el control del calculo
def calcular(**tipo_calculo):
    for k,v in tipo_calculo.items():  #Iteramos sobre cada item de los valores entregados por el kwargs
        if 'fact' in k:  #Si la llave posee el nombre fact, ocupamos el factorial
            factorial(v)
        elif 'prod' in k: #Si la llave posee el nombre prod, ocupamos la productoria
            pitatoria(v)
        else: pass

#Llamamos a la funcion para hacer los calculos
print('-'*80)
calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
print('-'*80)