from models.cell import Cell

class Wall(Cell):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self._width = width
        self._height = height

    """ Dimension Getter and Setter """
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    
    """ Print Symbol for Wall """
    def print_symbol(self):
        return " W "