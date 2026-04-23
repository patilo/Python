#creamos la clase calculadora
#esta contiene el iva y la funcion que calcula el total
#el iva es del 19%

class Calculadora:
    def __init__(self):
        #creamos el iva
        self.iva_porcentaje = 0.19

    #funcion que calcula el total
    def calcular_final(self, lista_carrito):
        # Esta función procesa la lista de diccionarios del carrito
        neto = sum(item['precio'] for item in lista_carrito)
        iva = neto * self.iva_porcentaje
        total = neto + iva
        return {
            "neto": neto,
            "iva": iva,
            "total": total
        }