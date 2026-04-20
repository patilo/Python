#calcula el promedio de una lista de numeros
lista_de_numeros = [1, 2, 3, 4, 5]
suma = sum(lista_de_numeros)
promedio = suma / len(lista_de_numeros)

#pidele la temperatura en grados celsius y conviertela a fahrenheit
temperatura = int(input("ingresa la temperatura en grados celsius: "))
fahrenheit = (temperatura * 9/5) + 32
print(f'la temperatura en grados fahrenheit es: {fahrenheit}')

print(f'el promedio de la lista es: {promedio}')
#utilizamos len para contar la cantidad de elementos
#utilizamos sum para sumar los elementos

#crea una lista de numeros y encuentra el numero mayor y menor
lista_de_numeros = [1, 2, 3, 4, 5]
print(f'el numero mayor es: {max(lista_de_numeros)}')
print(f'el numero menor es: {min(lista_de_numeros)}')
#utilizamos max para encontrar el numero mayor
#utilizamos min para encontrar el numero menor

#crea una lista de numeros y encuentra el numero mayor y menor
lista_de_numeros = [1, 2, 3, 4, 5]
print(f'el numero mayor es: {max(lista_de_numeros)}')
print(f'el numero menor es: {min(lista_de_numeros)}')
#utilizamos max para encontrar el numero mayor
#utilizamos min para encontrar el numero menor

#pidele al usuario que ingrese un numero y muestra si es par o impar
numero = int(input("ingresa un numero: "))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

#pidele una password al usuario y muestra si es correcta o no
password = input("ingresa tu password: ")
if password == "1234":
    print("password correcta")
else:
    print("password incorrecta")



#cajero bancario, pide saldo, retira dinero y muestra el saldo, para entrar pide password
#uso de if y match
password = input("ingresa tu password: ")
saldo = 1000
match password:
    case "1234":
        print("password correcta")
        opcion = input("ingresa una opcion: 1.consultar saldo, 2.retirar dinero, 3.salir")
        if opcion == "1":
            print("tu saldo es: ", saldo)
        elif opcion == "2":
            dinero = int(input("ingresa la cantidad de dinero que deseas retirar: "))
            if dinero > saldo:
                print("saldo insuficiente")
            else:
                saldo -= dinero
                print("saldo actual: ", saldo)
        elif opcion == "3":
            print("adios")
        else:
            print("opcion no valida")
    case _:
        print("password incorrecta")
        

#mision espacial, usa el while para que el usuario pueda ingresar opciones hasta que ingrese salir
#si ingresa 1, lanza el cohete
#si ingresa 2, apaga los motores
#si ingresa 3, sale
#uso de while y match

option = ""
while option != "3":
    option = input("ingresa una opcion: 1.lanzar cohete, 2.apagar motores, 3.salir")
    match option:
        case "1":
            print("lanzando cohete")
        case "2":
            print("motores apagados")
        case "3":
            print("adios")
        case _:
            print("opcion no valida")


#mision espacial acumulando energia para el despegue
#para acumular energia utilizamos += y el valor que queremos sumar
#cada vez que se ingrese 1 se sumara 10 a la energia
#como es un bucle while se ejecutara hasta que la energia sea 100
#agregamos el break para que se pueda salir del bucle
energia = 0
while energia < 100:
    opcion = input("ingresa una opcion: 1.cargar bateria, 2.despegar, 3.salir: ")
    match opcion:
        case "1":
            energia += 10
            print("energia actual: ", energia)
        case "2":
            if energia >= 100:
                print("despegando cohete")
            else:
                print("energia insuficiente")
                print("energia actual: ", energia)
        case "3":
            print("adios")
            break
        case _:
            print("opcion no valida")

#ejercicio con for
#crea una lista de numeros, recorre la lista y muestra solo los numeros pares
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista_de_numeros:
    if i % 2 == 0:
        print(i)

#ejercicio con for y break
#recorre una lista de numero y cuando encuentre el numero 5, se detiene
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista_de_numeros:
    if i == 5:
        break
    print(i)

#ejercicio con for y continue
#recorre una lista de numero y cuando encuentre el numero 5, lo imprime y continua con el bucle
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista_de_numeros:
    if i == 5:
        print("aparecio el 5")
        continue

    print(i)


#ejercicio mixto con for while e if
#Estás programando un script para un firewall que debe monitorear intentos de acceso. 
#El sistema tiene una lista de contraseñas bloqueadas (por ser comunes o inseguras) y un límite de intentos.

# Configuración inicial
password_correcta = "Admin_2026"
lista_negra = ["123456", "password", "admin", "qwerty"]
intentos_maximos = 3
intentos_realizados = 0
acceso_concedido = False

#bucle while para limitar los intentos
while intentos_realizados < intentos_maximos and not acceso_concedido:
    password_usuario = input(f"\nIntento {intentos_realizados + 1}/{intentos_maximos}. Ingrese su clave: ")
   # 2. Uso de FOR para revisar la lista negra
    es_insegura = False
    for p_prohibida in lista_negra:
        if password_usuario == p_prohibida:
            es_insegura = True
            break # Si la encuentra, no sigue buscando en la lista
    
    # 3. Uso de IF/ELIF/ELSE para la lógica de negocio
    if es_insegura:
        print("ALERTA: Contraseña bloqueada por motivos de seguridad (está en la lista negra).")
        intentos_realizados += 1
    elif password_usuario == password_correcta:
        print("ÉXITO: Identidad verificada. Bienvenida/o al sistema.")
        acceso_concedido = True
    else:
        print("ERROR: Contraseña incorrecta.")
        intentos_realizados += 1

if not acceso_concedido:
    print("cuenta bloqueada")   

#recorriendo un diccionario de notas, calculando el promedio y mostrando si aprobo o no
lista_de_notas = {"matematicas": 10, "ciencias": 8, "historia": 9, "lenguaje": 7}
promedio = sum(lista_de_notas.values()) / len(lista_de_notas)
if promedio >= 6:
    print("aprobo")
else:
    print("reprobó")

#crea una lista de verduras con su precio, recorre la lista y muestra solo las verduras con precio mayor a 1000
#ademas verifica y recorre la lista original para saber si la verdura existe
#uso de for y if

lista_pedida = ["lechuga", "tomate", "cebolla", "papa", "zanahoria"]
lista_precios = [1000, 2000, 3000, 4000, 5000]
for i in lista_pedida:
    if i in lista_precios:
        print(i, lista_precios[i])
    else:
        print(i, "no existe")