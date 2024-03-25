""" Jump Point Search """

from functools import cache
from models.grid import Grid
from models.cell import Cell
from models.goal import Goal
import itertools
from queue import PriorityQueue

from utils.build_path import build_path

class JPS:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.goals = self.grid._goal
        self.priority_queue = PriorityQueue()
        self.visited = set()
        self.path = {}
        self.counter = itertools.count()

    def manhattan_distance(self, cell: Cell, goal: Cell):
        return abs(cell.x - goal.x) + abs(cell.y - goal.y)

    def heuristic(self, cell: Cell):
        return min(self.manhattan_distance(cell, goal) for goal in self.goals)

    def calculate_f(self, cell: Cell, parent: Cell = None):
        g = 0 if parent is None else parent.g + 1
        h = self.heuristic(cell)
        cell.g = g  # Update the g value of the cell
        return g + h

    def add_to_queue(self, cell, parent=None):
        cost = self.calculate_f(cell, parent)
        count = next(self.counter)
        self.priority_queue.put((cost, count, cell))
        if parent:
            self.path[cell] = parent

    def explore_direction(self, cell: Cell, direction):
        # Directly access the cell's neighbor based on the direction
        if direction == "UP":
            return cell.north
        elif direction == "LEFT":
            return cell.west
        elif direction == "DOWN":
            return cell.south
        elif direction == "RIGHT":
            return cell.east

    def find_jump_point(self, cell: Cell, direction):
        next_cell = self.explore_direction(cell, direction)
        while next_cell:
            if next_cell in self.visited:
                break  
            if next_cell in self.goals:
                return next_cell  
            self.visited.add(next_cell)  
            next_cell = self.explore_direction(next_cell, direction)
        return None

    def search(self):
        print("JPS Start")
        agent_start = self.grid.get_agent()
        self.visited.add(agent_start)
        count = next(self.counter)
        start_heuristic = self.heuristic(agent_start)
        self.priority_queue.put((start_heuristic, None, count, agent_start))

        while not self.priority_queue.empty():
            _, _, _, current_cell = self.priority_queue.get()

            if current_cell in self.goals:
                print(f"Goal found: {current_cell}")
                return self.reconstruct_path(current_cell)

            for direction in ["UP", "LEFT", "DOWN", "RIGHT"]:
                jump_point = self.find_jump_point(current_cell, direction)
                if jump_point:
                    self.add_to_queue(jump_point, current_cell)

        print("No path found")
        return None
