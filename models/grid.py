from models.cell import Cell
from models.agent import Agent
from models.goal import Goal
from models.cell import Cell
from models.wall import Wall

class Grid:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.grid = []
        self.build_grid()

    """ iterate over each row and create columns for each row """
    def build_grid(self):
        self.grid = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]

    """ create and set agent position within grid """
    def set_agent(self, x, y):
        if 0 <= y < self.height and 0 <= x < self.width:
            self.grid[y][x] = Agent(x, y)

    """ create goal cells within grid """
    def add_goal(self, x, y):
        if 0 <= y < self.height and 0 <= x < self.width:
            self.grid[y][x] = Goal(x, y)

    """ create walls given the wall specs within grid bounds """
    def add_wall(self, x, y, width, height):
        for i in range(x, min(x + width, self.width)):
            for j in range(y, min(y + height, self.height)):
                self.grid[j][i] = Wall(i, j, width, height)

    """ set pointers for neighboring cells by direction"""
    def set_neighbors(self):
        for row_index in range(self.height):  
            for column_index in range(self.width):  

                # Set pointers for north
                if row_index > 0:
                    self.grid[row_index][column_index].north = self.grid[row_index - 1][column_index]
                else:
                    self.grid[row_index][column_index].north = None

                # Set pointers for south
                if row_index < self.height - 1:
                    self.grid[row_index][column_index].south = self.grid[row_index + 1][column_index]
                else:
                    self.grid[row_index][column_index].south = None

                # Set pointers for west
                if column_index > 0:
                    self.grid[row_index][column_index].west = self.grid[row_index][column_index - 1]
                else:
                    self.grid[row_index][column_index].west = None

                # Set pointers for east
                if column_index < self.width - 1:
                    self.grid[row_index][column_index].east = self.grid[row_index][column_index + 1]
                else:
                    self.grid[row_index][column_index].east = None

    def print_grid(self):
        for row_index in range(self.height):
            print("\n")
            for column_index in range(self.width):
                if isinstance(self.grid[row_index][column_index], Wall):
                    print(" W ", end="")
                elif isinstance(self.grid[row_index][column_index], Agent):
                    print(" A ", end="")
                elif isinstance(self.grid[row_index][column_index], Goal):
                    print(" G ", end="")
                elif isinstance(self.grid[row_index][column_index], Cell):
                    print(" . ", end="")
  