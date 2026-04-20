#creamos la clase pasillo
#esta contiene el nombre del pasillo y el inventario



class Pasillo:
    def __init__(self):
        # Un solo objeto Pasillo contiene todas las categorías
        self.categorias = {
            "lacteos": {"leche": 1100, "queso": 2500, "yogurt": 450},
            "verduras": {"tomate": 1500, "lechuga": 900, "zanahoria": 800},
            "articulos de aseo": {"cloro": 1300, "detergente": 7500},
            "carnes": {"pollo": 5000, "vacuno": 9800, "cerdo": 4500},
            "cereales": {"avena": 2200, "sucaritas": 3500, "granola": 4000},
            "refrescos": {"coca cola": 2500, "jugo": 1200, "agua": 800}
        }

    #funcion que me devuelva los pasillos
    def obtener_pasillos(self):
        return list(self.categorias.keys())

    #funcion que me devuelva los productos de un pasillo
    def obtener_productos(self, nombre_pasillo):
        return self.categorias.get(nombre_pasillo, {})