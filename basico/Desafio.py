#guía de Laboratorio: Programación en Python
#Ejercicio: Simulador de Compra Inteligente por Categorías
#Contexto:
#Una cadena de supermercados requiere un prototipo de sistema de ventas por consola. El sistema debe permitir a los clientes navegar de forma lógica por los diferentes pasillos de la tienda, visualizar productos y gestionar un carrito de compras dinámico.

#Objetivo de aprendizaje:
#Implementar diccionarios anidados para el almacenamiento de datos estructurados.
#Gestionar el flujo de ejecución mediante ciclos infinitos controlados (while True).
#Aplicar lógica de validación de datos y acumuladores para cálculos financieros básicos.


#Descripción del Desafío
#Debes desarrollar un programa en Python que cumpla con las siguientes especificaciones:

#1. Estructura de Datos (Inventario)
#Crea una estructura llamada supermercado utilizando diccionarios anidados. La estructura debe seguir el siguiente esquema de categorías y precios:

#Lácteos: Leche ($1.100), Yogurt ($450), Queso ($2.500).

#Verduras: Tomate ($1.500), Lechuga ($900), Papas ($1.200).

#Carnes: Pollo ($5.000), Vacuno ($9.500), Cerdo ($4.500).

#Aseo: Cloro ($1.300), Detergente ($7.500).

#2. Interfaz y Navegación (Menú de Pasillos)
#El programa debe iniciar mostrando un Menú Principal con los nombres de los pasillos disponibles y una opción adicional para "Finalizar Compra".
#Si el usuario selecciona un pasillo válido, debe ingresar a un submenú.
#Si selecciona "Finalizar", el programa debe detener su ejecución y emitir el reporte final.

#3. Proceso de Selección (Submenú de Productos)
#Al entrar en un pasillo, el sistema debe:
#Listar todos los productos de esa categoría con sus respectivos precios.
#Permitir al usuario escribir el nombre de un producto para agregarlo al "Carrito".
#Ofrecer una opción para "Volver" al menú principal de pasillos.
#Validación: Si el usuario ingresa un producto que no existe en ese pasillo, el sistema debe mostrar un mensaje de error y permitir reintentar.

#4. Salida y Totales (Generación de Boleta)
#Una vez que el usuario decida finalizar la compra, el programa debe imprimir en pantalla:
#Una lista detallada de todos los productos seleccionados.
#El subtotal de la compra.
#El cálculo del IVA (19%) y el Total Final a Pagar.







# 1. Base de Datos del Supermercado
supermercado = {
    "lacteos": {"leche": 1100, "yogurt": 450, "queso": 2500, "mantequilla": 1200},
    "verduras": {"tomate": 1500, "lechuga": 900, "papas": 1200, "cebolla": 1000},
    "carnes": {"pollo": 5000, "vacuno": 9500, "cerdo": 4500, "hamburguesa": 800},
    "articulos_aseo": {"cloro": 1300, "detergente": 7500, "lavaloza": 2200}
}

carrito = []
total_general = 0

print("BIENVENIDO A SUPERMERCADO PYTHON")

while True:
    # 2. Menú de Pasillos
    print("\n--- PASILLOS DISPONIBLES ---")
    print("1. Lacteos\n2. Verduras\n3. Carnes\n4. Articulos_aseo\n5. SALIR Y PAGAR")
    
    opcion = input("\nSeleccione un pasillo (nombre o número) o '5' para pagar: ").lower()

    if opcion == "5" or opcion == "salir":
        break

    # Validación de entrada (por si el usuario escribe el nombre del pasillo)
    if opcion == "1": opcion = "lacteos"
    elif opcion == "2": opcion = "verduras"
    elif opcion == "3": opcion = "carnes"
    elif opcion == "4": opcion = "articulos_aseo"

    if opcion in supermercado:
        # 3. Menu Interno del Pasillo
        while True:
            print(f"\n--- ESTÁS EN EL PASILLO: {opcion.upper()} ---")
            productos_pasillo = supermercado[opcion]
            
            # Listar diccionario del pasillo
            for prod, precio in productos_pasillo.items():
                print(f"- {prod.capitalize()}: ${precio}")
            
            seleccion = input("\nEscriba el nombre del producto para comprar o 'volver': ").lower()
            
            if seleccion == "volver":
                break
            
            if seleccion in productos_pasillo:
                precio_prod = productos_pasillo[seleccion]
                carrito.append({"nombre": seleccion, "precio": precio_prod})
                total_general += precio_prod
                print(f"'{seleccion}' agregado al carrito.")
            else:
                print(" Producto no encontrado en este pasillo.")
    else:
        print("⚠ Opción no válida. Intente nuevamente.")

# 4. Detalle Final y Boleta
print("\n" + "="*30)
print("BOLETA ELECTRÓNICA")
if not carrito:
    print("No se realizaron compras.")
else:
    for item in carrito:
        print(f"{item['nombre'].capitalize():<15} ${item['precio']:>5}")

print("-" * 30)
print(f"TOTAL A PAGAR:   ${total_general}")
print("="*30)
print("¡Gracias por su compra!")