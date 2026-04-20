class FiguraGeometrica:
        def __init__(self, alto, ancho):
                #validamos que sean valores positivos
                if self.ValidarValor(ancho):
                        self.ancho = ancho
                else:
                        self.ancho = 0
                        print(f'valor erroneo de {ancho}')

                if self.ValidarValor(alto):
                        self.alto = alto
                else:
                        self.alto = 0
                        print(f'valor erroneo de {alto}')

       #creamos los getter / setter
        @property
        def ancho(self):
             return self._ancho

        @ancho.setter
        def ancho(self,ancho):
            if self.ValidarValor(ancho):
                self._ancho = ancho

        @property
        def alto(self):
                return self._alto

        @alto.setter
        def alto(self, alto):
            if self.ValidarValor(ancho):
                self._alto = alto

        # creamos el str para que no muestre el valor en la memoria y retorne valores
        def __str__(self):
                return f'el alto es: {self.alto} y ancho: {self.ancho}'

        # como validamos, se pasa a los setter para que asigne el valor
        def ValidarValor (self, valor):
                return True if 0<valor else False
