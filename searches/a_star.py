from models.grid import Grid
from models.cell import Cell
from models.goal import Goal
import itertools
from queue import PriorityQueue

from utils.build_path import build_path

class AS:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.goals = self.grid._goal
        self.priority_queue = PriorityQueue()
        self.visited = set()
        self.path = {}
        self.counter = itertools.count()

    """ Manhattan Distance method for calculating heuristic """
    def manhattan_distance(self, cell: Cell, goal: Goal):
        return abs(cell.x - goal.x) + abs(cell.y - goal.y)

    """ when all else equal explore directional bias """
    def directional_bias(self, cell: Cell, neighbor: Cell):
        bias = {'UP': 0, 'LEFT': 1, 'DOWN': 2, 'RIGHT': 3}
        direction = self.grid.get_direction(cell, neighbor)
        return bias.get(direction)

    """ Heuristic calculation """
    def heuristic(self, cell: Cell):
        return min(self.manhattan_distance(cell, goal) for goal in self.grid._goal)
    
    """ Calculate f(n) for priority exploration"""
    def calculate_f(self, cell: Cell, parent: Cell = None) -> int:

        if parent == None:
            cell.g = 0
        else:
            cell.g = parent.g + 1

        h = self.heuristic(cell)
        return cell.g + h
    
    """ adding cells to priority queue based on cost & direction """
    def add_to_queue(self, cell, neighbor):
        count = next(self.counter)
        direction_bias = self.directional_bias(cell, neighbor)
        cost = self.calculate_f(neighbor, cell)
        self.priority_queue.put((cost, direction_bias, count, neighbor))

    """ AS search implementation """
    def search(self):
        agent_start = self.grid.get_agent()
        count = next(self.counter)
        start_cost = self.calculate_f(agent_start)
        self.priority_queue.put((start_cost, None, count, agent_start))
        self.visited.add(agent_start)

        while not self.priority_queue.empty():
            _, _, _, current_cell = self.priority_queue.get()

            if isinstance(current_cell, Goal):
                print(f"\n<Node ({current_cell.x},{current_cell.y})>")
                traversedPath = build_path(current_cell, self.path)
                print(f"AS Path : {traversedPath}")
                return True
            
            for neighbor in [current_cell.north, current_cell.east, current_cell.south, current_cell.west]:
                if neighbor != None and neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.add_to_queue(current_cell, neighbor)
                    self.path[neighbor] = current_cell
        return False