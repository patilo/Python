**Objetivo del Desafío**

Desarrollar un sistema de compras profesional utilizando el paradigma de Programación Orientada a Objetos (POO). El enfoque principal es la modularización, separando la definición de las entidades (clases) de la lógica de interacción con el usuario (interfaz de consola).

equerimientos de Arquitectura
El proyecto debe estar dividido en dos archivos fundamentales:

**1. El Motor de Datos (clases.py)**
En este archivo se deben definir las plantillas lógicas del sistema:

Clase Pasillo: * Debe contener una estructura de datos centralizada (diccionarios anidados) que agrupe las siguientes categorías: Lácteos, Verduras, Artículos de Aseo, Carnes, Cereales y Refrescos.

Cada categoría debe listar sus productos con sus respectivos precios.

Debe implementar métodos para retornar la lista de pasillos y los productos de una categoría específica.

Clase Calculadora: * Su única responsabilidad es el procesamiento aritmético.

Debe recibir el listado de productos seleccionados (carrito) y calcular: Subtotal Neto, Impuesto al Valor Agregado (IVA 19%) y Total Final.

**2. El Orquestador del Sistema (main.py)**
Este archivo debe importar las clases y gestionar la experiencia del usuario mediante un flujo lógico:

Navegación de Pasillos: Mostrar un menú dinámico con las categorías disponibles.

Selección de Productos: Al entrar a un pasillo, el usuario puede elegir productos por su nombre para añadirlos a una lista de compras o decidir "salir" para cambiar de pasillo.

Cierre de Caja: Al seleccionar la opción de pago, el sistema debe delegar los cálculos a la clase Calculadora y emitir un reporte final detallado.