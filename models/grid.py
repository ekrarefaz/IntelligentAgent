from models.cell import Cell
from models.agent import Agent
from models.goal import Goal
from models.cell import Cell
from models.wall import Wall

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        self.build_grid()

    def build_grid(self):
        # Initialize the grid with Cell instances
        self.grid = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]

    def set_agent(self, x, y):
        # Ensure the cell exists
        if 0 <= y < self.height and 0 <= x < self.width:
            self.grid[y][x] = Agent(x, y)

    def add_goal(self, x, y):
        # Ensure the cell exists
        if 0 <= y < self.height and 0 <= x < self.width:
            self.grid[y][x] = Goal(x, y)

    def add_wall(self, x, y, width, height):
        # Ensure the wall fits within the grid bounds
        for i in range(x, min(x + width, self.width)):
            for j in range(y, min(y + height, self.height)):
                self.grid[j][i] = Wall(i, j, width, height)