import pasillo as Pasillo
import calculadora as Calculadora

#creamos la funcion menu_supermercado
def menu_supermercado():
    #llamamos a las clases y creamos los objetos
    #nos sirve para crear un objeto de la clase Pasillo y Calculadora
    gestor_inventario = Pasillo.Pasillo()    
    procesador_pagos = Calculadora.Calculadora()
    carrito = []

    #creamos el bucle while para que el menu se repita hasta que el usuario decida salir
    while True:
        print("\n===== MENÚ DE PASILLOS =====")
        #obtenemos los pasillos
        #para eso llamamos a la funcion obtener_pasillos del objeto gestor_inventario
        lista_pasillos = gestor_inventario.obtener_pasillos()
        
        #mostramos los pasillos y la opcion de pagar
        for i, nombre in enumerate(lista_pasillos, 1):
            print(f"{i}. {nombre.capitalize()}")
        print(f"{len(lista_pasillos) + 1}. IR A PAGAR")

        #obtenemos la opcion del usuario y la guardamos en la variable opcion
        opcion = input("\nSeleccione un pasillo o elija pagar: ")

        #logica para finalizar compra
        if opcion == str(len(lista_pasillos) + 1):
            break

        #logica para entrar a un pasillo
        #el try es para que el programa no se caiga si el usuario ingresa algo que no es un numero
        try:
            indice = int(opcion) - 1
            nombre_pasillo = lista_pasillos[indice]
            
            #creamos el bucle while para que el menu se repita hasta que el usuario decida salir
            while True:
                productos = gestor_inventario.obtener_productos(nombre_pasillo)
                print(f"\n--- PRODUCTOS EN {nombre_pasillo.upper()} ---")
                for prod, precio in productos.items():
                    print(f"- {prod.capitalize()}: ${precio}")
                
                seleccion = input("\nEscriba el producto para comprar o 'salir' para volver: ").lower()

                if seleccion == "salir":
                    break
                
                if seleccion in productos:
                    carrito.append({"nombre": seleccion, "precio": productos[seleccion]})
                    print(f" '{seleccion}' añadido.")
                else:
                    print("Ese producto no está en este pasillo.")
                    
        except (ValueError, IndexError):
            print("opcion no valida, intente de nuevo.")

    #pantalla de Pago Final
    if carrito:
        resultados = procesador_pagos.calcular_final(carrito)
        print("\n" + "="*35)
        print("        DETALLE DE COMPRA")
        print("="*35)
        for item in carrito:
            print(f"{item['nombre'].capitalize():<20} ${item['precio']:>8}")
        
        print("-" * 35)
        print(f"SUBTOTAL NETO:        ${int(resultados['neto']):>8}")
        print(f"IVA (19%):            ${int(resultados['iva']):>8}")
        print(f"TOTAL A PAGAR:        ${int(resultados['total']):>8}")
        print("="*35)
    else:
        print("\nNo compraste nada. ¡Hasta la próxima!")

if __name__ == "__main__":
    menu_supermercado()