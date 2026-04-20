#Patricio Carrasco
from logging import _Level
import preguntas as p

def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    if n_pregunta <=p_level:
        Level= "basicas"
    elif n_pregunta <=p_level*2:
        Level="intermedias"
    else:
        level="avanzadas"
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias
