class Quadrant:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_quadrant_coordinate(self):
        
        coordinateX = self.coordinates.coordinateX
        coordinateY = self.coordinates.coordinateY

        if (coordinateX > 0 and coordinateY > 0):
            return "Pertence ao Primeiro Quadrante"
        elif (coordinateX < 0 and coordinateY > 0):
            return "Pertence ao Segundo Quadrante"
        elif (coordinateX < 0 and coordinateY < 0):
            return "Pertence ao Terceiro Quadrante"
        elif (coordinateX > 0 and coordinateY < 0):
            return "Pertence ao Primeiro Quadrante"
        else:
            return "Número nulo informado"
