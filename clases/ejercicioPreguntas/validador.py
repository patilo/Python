#Patricio Carrasco
def validate(opciones, eleccion):
    # Definir validación de eleccion
    while eleccion not in opciones:
        eleccion = input("opcion no valida, seleccione una correcta ['a','b','c','d'] : ")
    return eleccion 


if __name__ == '__main__':
    
    e = input('Ingresa una Opción: ').lower()
    l = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    n = ['0','1']# tambien se pueden comprobar con numeros
    # Si se ingresan valores no validos a eleccion debe seguir preguntando

    validate(opciones=l, eleccion=e)
    
