from models.cell import Cell

class Agent(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    def print_symbol(self):
        return " A "
