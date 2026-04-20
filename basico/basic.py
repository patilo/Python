#tipos de datos en python
string = "hola"
numerico = 1
flotante = 1.5
booleano = True


#funcion de imprimir
#es para mostrar valores en la consola
print(string)
print(f'el valor de numerico es: {numerico}')

#variables y operadores
#creamos 2 variables enteras
#creamos una variable llamada suma y le asignamos el valor de a + b
a = 1
b = 2

suma = a + b
print(suma)
print(f'la suma de a y b es: {suma}')

#funciones matematicas
#creamos una lista de numeros y aplicamos funciones matematicas
lista_de_numeros = [1, 2, 3, 4, 5]
#sumamos todos los numeros de la lista
print(sum(lista_de_numeros))
#contamos la cantidad de numeros de la lista
print(len(lista_de_numeros))
#encontramos el numero mayor de la lista
print(max(lista_de_numeros))
#encontramos el numero menor de la lista
print(min(lista_de_numeros))
#ordenamos la lista de menor a mayor
print(sorted(lista_de_numeros))
print(sorted(lista_de_numeros, reverse=True))



#listas, tuplas y diccionarios
#lista es una coleccion de elementos que se puede modificar y utiliza corchetes []
#tupla es una coleccion de elementos que no se puede modificar y utiliza parentesis ()
#diccionario es una coleccion de elementos que se puede modificar y utiliza llaves {}
#el diccionario se compone de clave y valor, el valor es el que se puede modificar
lista = [1, 2, 3, 4, 5]
lista_nombres = ["patilo", "carrasco", "pato"]
tupla = (1, 2, 3, 4, 5)
tupla_nombres = ("patilo", "carrasco", "pato")
diccionario = {"manzana": 1, "banana": 2, "pera": 3, "uva": 4, "naranja": 5}
diccionario_nombres = {"nombre": "patilo", "apellido": "carrasco", "edad": 25}

#funciones para lista, tupla y diccionario
len() #cuenta la cantidad de elementos
#ejemplo
len(lista)
len(tupla)
len(diccionario)

sorted() #ordena la lista de menor a mayor
#ejemplo
sorted(lista)
sorted(tupla)
sorted(diccionario)

append() #agrega un elemento a la lista
#ejemplo
lista.append("pera")
diccionario.append("pera")

insert() #inserta un elemento en una posicion especifica
#ejemplo
lista.insert(1, "pera")
diccionario.insert(1, "pera")

remove() #elimina un elemento de la lista
#ejemplo
lista.remove("pera")
diccionario.remove("pera")

pop() #elimina un elemento de la lista por su indice
#ejemplo
lista.pop(1)
diccionario.pop("pera")

count() #cuenta la cantidad de un elemento en la lista
#ejemplo
lista.count("pera")
diccionario.count("pera")

index() #encuentra el indice de un elemento en la lista
#ejemplo
lista.index("pera")
diccionario.index("pera")

reverse() #invierte el orden de la lista
#ejemplo
lista.reverse()




#condicionales
#estos son para tomar decisiones en base a una condicion
#if, elif, else
#if es para verificar si una condicion es verdadera
#elif es para verificar si una condicion es verdadera
#else es para verificar si una condicion es verdadera

edad = 18
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

#ejemplo de condicionales con promedio
promedio = 7
if promedio >= 7:
    print("aprobado")
elif promedio >= 6:
    print("regular")
else:
    print("reprobado")

#ejemplo de condicionales con lista
lista_de_frutas = ["manzana", "banana", "pera", "uva", "naranja"]
if "manzana" in lista_de_frutas:
    print("manzana esta en la lista")
else:
    print("manzana no esta en la lista")


#ejemplo de condicionales con diccionario
diccionario_de_frutas = {
    "manzana": 1,
    "banana": 2,
    "pera": 3,
    "uva": 4,
    "naranja": 5
}
if "manzana" in diccionario_de_frutas:
    print("manzana esta en el diccionario")
elif "banana" in diccionario_de_frutas:
    print("banana esta en el diccionario")
elif "pera" in diccionario_de_frutas:
    print("pera esta en el diccionario")
elif "uva" in diccionario_de_frutas:
    print("uva esta en el diccionario")
elif "naranja" in diccionario_de_frutas:
    print("naranja esta en el diccionario")
else:
    print("no se encontro la fruta")

#bucle while
#el bucle while se ejecuta mientras la condicion sea verdadera
#debe tener una condicion para que no se ejecute infinitamente
#debe tener una variable que se incremente o decremente para que la condicion sea falsa
lista_de_numeros = [1, 2, 3, 4, 5]
i = 0
while i < len(lista_de_numeros):
    print(lista_de_numeros[i])
    i += 1

lista_de_frutas = ["manzana", "banana", "pera", "uva", "naranja"]
while i < len(lista_de_frutas):
    print(lista_de_frutas[i])
    i += 1

#ejercicio while + if
lista_de_numeros = [1, 2, 3, 4, 5]
while i < len(lista_de_numeros):
    if lista_de_numeros[i] % 2 == 0:
        print(lista_de_numeros[i])
    i += 1

#uso de break
lista_de_numeros = [1, 2, 3, 4, 5]
while i < len(lista_de_numeros):
    if lista_de_numeros[i] == 3:
        break
    print(lista_de_numeros[i])
    i += 1


#uso de continue
lista_de_numeros = [1, 2, 3, 4, 5]
while i < len(lista_de_numeros):
    if lista_de_numeros[i] == 3:
        continue
    print(lista_de_numeros[i])
    i += 1

#bucle for
#busca elementos en una lista y los recorre
#es mas limpio que el bucle while
#nos sirve para recorrer listas, tuplas, diccionarios, etc

lista_de_numeros = [1, 2, 3, 4, 5]
for i in lista_de_numeros:
    print(i)

#este guarda los valores recorridos en una variable
#podemos usar range para generar una secuencia de numeros
for i in range(10):
    print(i)

#es te guarda los valores recorridos en una variable
#podemos usar range para generar una secuencia de numeros
for i in range(1, 20, 2):
    print(i)

#este guarda los valores recorridos en una variable
#podemos usar range para generar una secuencia de numeros
for i in range(20, 1, -2):
    print(i)


#ejemplo de bucle for con lista
lista_de_numeros = [1, 2, 3, 4, 5]
for i in lista_de_numeros:
    print(i)

#ejemplo de bucle for con diccionario
diccionario_de_frutas = {
    "manzana": 1,
    "banana": 2,
    "pera": 3,
    "uva": 4,
    "naranja": 5
}
for i in diccionario_de_frutas:
    print(i)

#for con if y else
for i in range(10):
    if i % 2 == 0:
        print(i)
    else:
        print(i)

#for con if y else con break
for i in range(10):
    if i % 2 == 0:
        print(i)
    else:
        print(i)
        break

#for con if y else con continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#funcion match case
#esta funcion busca coincidencias en una variable
#estas deben ser iguales para que se ejecute el codigo

option = 1
match option:
    case 1:
        print("opcion 1")
    case 2:
        print("opcion 2")
    case 3:
        print("opcion 3")
    case _:
        print("opcion no valida")

#funcion match case con lista
lista_de_frutas = ["manzana", "banana", "pera", "uva", "naranja"]
match lista_de_frutas:
    case ["manzana", "banana", "pera", "uva", "naranja"]:
        print("lista de frutas")
    case _:
        print("lista no valida")


        
