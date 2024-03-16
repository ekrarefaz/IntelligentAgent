from models.cell import Cell

class Wall(Cell):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self.width
    
    @property
    def height(self):
        return self.height
    
    def print_symbol(self):
        return " W "