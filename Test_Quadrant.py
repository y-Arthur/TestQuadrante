from unittest import result
from Coordinate import Coordinate
from Quadrant import Quadrant



def teste_Deve_Retorna_Primeiro_Quadrante():
    x = 2
    y = 2
    coordenadas = Coordinate(x,y)
    quadrante = Quadrant(coordenadas)

    result = quadrante.get_quadrant_coordinate()


    assert result == "Pertence ao Primeiro Quadrante"





def teste_Deve_Retorna_Segundo_Quadrante():
    x = -7
    y = 1
    coordenadas = Coordinate(x,y)
    quadrante = Quadrant(coordenadas)

    result = quadrante.get_quadrant_coordinate()


    assert result == "Pertence ao Segundo Quadrante"


    
def teste_Deve_Retorna_Terceiro_Quadrante():
    x = -8
    y = -1
    coordenadas = Coordinate(x,y)
    quadrante = Quadrant(coordenadas)

    result = quadrante.get_quadrant_coordinate()


    assert result == "Pertence ao Terceiro Quadrante"




def teste_Deve_Retorna_Quarto_Quadrante():
    x = 3
    y = -2
    coordenadas = Coordinate(x,y)
    quadrante = Quadrant(coordenadas)

    result = quadrante.get_quadrant_coordinate()


    assert result == "Pertence ao Primeiro Quadrante"


def teste_DeveRetorna_Nulo():
    x = 0
    y = 2
    coordenadas = Coordinate(x,y)
    quadrante = Quadrant(coordenadas)

    result = quadrante.get_quadrant_coordinate()


    assert result == "Número nulo informado"