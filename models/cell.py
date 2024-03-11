class Cell:
    def __init__(self,x, y, cell_type='empty'):
        self.x = x
        self.y = y

        self.north = None
        self.south = None
        self.east = None
        self.west = None

        self.visited = False
        self.on_path = False
