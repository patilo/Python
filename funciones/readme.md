**Fundamentos de Clases y Objetos en Python**

Este módulo profundiza en la estructura fundamental de la programación moderna. Entender las clases es el primer paso para construir software modular, reutilizable y profesional.

Una clase es como un plano o molde para crear objetos.
Define las propiedades (datos) y los comportamientos (funciones) que tendrán los objetos creados a partir de ella. Un objeto es una instancia de una clase.
Una clase se define con la palabra clave **class**.


**1. Conceptos Básicos: El Paradigma de Clases**
¿Qué es una Clase?
Una Clase es una entidad abstracta que actúa como un blueprint (plano arquitectónico) o molde. Su función es agrupar datos y comportamientos relacionados en una sola unidad lógica.
Se define utilizando la palabra clave reservada class.
Los nombres de las clases deben seguir la convención PascalCase (ej: GestionUsuarios).  
  
¿Qué es un Objeto (Instancia)?  
El Objeto es la materialización de la clase. Es la entidad concreta que vive en la memoria de la computadora una vez que el programa se ejecuta.
Instanciación: Es el proceso de crear un objeto a partir de una clase.

**2. El Constructor __init__**
El método __init__ es un método mágico (dunder method) que actúa como el constructor de la clase. Su propósito principal es garantizar que el objeto nazca con un estado inicial válido.

Características Clave:
Ejecución Automática: No se llama manualmente; Python lo invoca en el momento exacto en que se crea el objeto.

Inicialización de Atributos: Aquí es donde definimos las propiedades únicas del objeto (ej: self.nombre, self.precio).

El Parámetro self:
Es el pilar de la programación orientada a objetos en Python.

Representa a la instancia específica que se está creando.

Permite que el código dentro de la clase sepa exactamente a qué objeto pertenecen los datos que está manipulando. Sin self, la clase no tendría "memoria" de sus propios atributos.

**3. Atributos y Métodos: El "Ser" y el "Hacer"**
Para entender la estructura interna de una clase, debemos separar sus componentes:
Atributos (Propiedades): Son las variables que describen al objeto. Representan el estado.

Ejemplo: En una clase Auto, los atributos serían color, marca y kilometraje.

Métodos (Comportamientos): Son funciones definidas dentro del cuerpo de la clase. Representan la lógica y capacidad de acción.

Siempre deben recibir self como primer parámetro para poder acceder o modificar los atributos del objeto.

Ejemplo: En la clase Auto, los métodos serían arrancar(), frenar() o repostar_combustible().

**4. Pilares de la Estructura de Objetos**
Para dominar la arquitectura de software, es vital comprender cómo interactúan las clases entre sí:

A. Herencia (Especialización)
Es un mecanismo que permite que una clase (clase hija) tome "prestados" los atributos y métodos de otra clase (clase padre).

Propósito: Reutilización de código y creación de jerarquías lógicas.

Uso Real: Si tienes una clase Empleado, puedes crear una clase hija Gerente que herede todo lo de empleado pero añada funciones específicas de supervisión.

B. Polimorfismo (Flexibilidad)
El polimorfismo permite que diferentes clases tengan métodos con el mismo nombre pero con implementaciones distintas.

Concepto: Significa "muchas formas".

Uso Real: Un método llamado enviar_notificacion() podría funcionar enviando un Email en una clase y un SMS en otra. El programador solo llama a enviar_notificacion() sin preocuparse de cómo se ejecuta internamente cada una.