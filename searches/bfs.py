from functools import cache
from models.grid import Grid
from models.cell import Cell
from models.goal import Goal
from collections import deque

class BFS:

    def __init__(self, grid: Grid):
        self.grid = grid
        self.queue = deque()
        self.visited = set()
        self.came_from = {}

    def search(self):
        agent_start: Cell = self.grid.get_agent()
        self.queue.append(agent_start)

        while self.queue:
            current_cell: Cell = self.queue.popleft()
            self.visited.add(current_cell)

            if isinstance(current_cell, Goal):
                print("Goal Reached")
                return True

            for direction in ["up", "left", "down", "right"]:
                if direction == "up" and current_cell.north and current_cell.north not in self.visited:
                    self.queue.append(current_cell.north)
                elif direction == "left" and current_cell.west and current_cell.west not in self.visited:
                    self.queue.append(current_cell.west)
                elif direction == "down" and current_cell.south and current_cell.south not in self.visited:
                    self.queue.append(current_cell.south)
                elif direction == "right" and current_cell.east and current_cell.east not in self.visited:
                    self.queue.append(current_cell.east)

        return False


        