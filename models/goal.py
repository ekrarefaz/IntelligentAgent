from models.cell import Cell

class Goal(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    """ Co-ordinate Getter and Setter """
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    
    def print_symbol(self):
        return " G "
