from models.cell import Cell
from models.agent import Agent
from models.goal import Goal
from models.cell import Cell
from models.wall import Wall

class Grid:
    def __init__(self, height, width):
        self._width = width
        self._height = height
        self._grid = []
        self._agent = None
        self._goal = []
        self.build_grid()

    """ iterate over each row and create columns for each row """
    def build_grid(self):
        self._grid = [[Cell(x, y) for x in range(self._width)] for y in range(self._height)]

    """ create and set agent position within grid """
    def set_agent(self, x, y):
        if 0 <= y < self._height and 0 <= x < self._width:
            self._agent = self._grid[y][x] = Agent(x, y)
    
    """ method for getting agent position """
    def get_agent(self):
        return self._agent

    """ create goal cells within grid """
    def add_goal(self, x, y):
        if 0 <= y < self._height and 0 <= x < self._width:
            self._grid[y][x] = Goal(x, y)

    """ create walls given the wall specs within grid bounds """
    def add_wall(self, x, y, width, height):
        for i in range(x, min(x + width, self._width)):
            for j in range(y, min(y + height, self._height)):
                self._grid[j][i] = Wall(i, j, width, height)

    """ set pointers for neighboring cells by direction"""
    def set_neighbors(self):
        for row_index in range(self._height):
            for column_index in range(self._width):
                cell = self._grid[row_index][column_index]

                # Check North neighbor
                if row_index > 0 and not isinstance(self._grid[row_index - 1][column_index], Wall):
                    cell.north = self._grid[row_index - 1][column_index]
                else:
                    cell.north = None

                # Check South neighbor
                if row_index < self._height - 1 and not isinstance(self._grid[row_index + 1][column_index], Wall):
                    cell.south = self._grid[row_index + 1][column_index]
                else:
                    cell.south = None

                # Check West neighbor
                if column_index > 0 and not isinstance(self._grid[row_index][column_index - 1], Wall):
                    cell.west = self._grid[row_index][column_index - 1]
                else:
                    cell.west = None

                # Check East neighbor
                if column_index < self._width - 1 and not isinstance(self._grid[row_index][column_index + 1], Wall):
                    cell.east = self._grid[row_index][column_index + 1]
                else:
                    cell.east = None

    """ prints a ascii representation of the grid """
    def print_grid(self):
        for row_index in self._grid:
            print("\n")
            for cell in row_index:
                print(cell.print_symbol(), end="")
            print("\n")
    