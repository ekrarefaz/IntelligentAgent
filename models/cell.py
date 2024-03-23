class Cell:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._north = None
        self._south = None
        self._east = None
        self._west = None

        self._g = None

    """ Co-ordinate Getter and Setter """
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    """ g(n) Setter and Getter """
    @property
    def g(self):
        return self._g
    @g.setter
    def g(self, value):
        self._g = value

    """ North Getter and Setter """
    @property
    def north(self):
        return self._north
    @north.setter
    def north(self, value):
        self._north = value
    
    """ South Getter and Setter """
    @property
    def south(self):
        return self._south
    @south.setter
    def south(self, value):
        self._south = value

    """ East Getter and Setter """
    @property
    def east(self):
        return self._east
    @east.setter
    def east(self, value):
        self._east = value

    """ West Getter and Setter """
    @property
    def west(self):
        return self._west
    @west.setter
    def west(self, value):
        self._west = value

    """ Print Co-ordinates """
    def get_coordinates(self):
        return (self.x, self.y)
    
    """ Print Symbol for Empty Cell """
    def print_symbol(self):
        return " . "
