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
        self.path = {}

    def search(self):
        agent_start: Cell = self.grid.get_agent()
        self.queue.append(agent_start)
        self.visited.add(agent_start)
        node_count = 1

        while self.queue:
            current_cell: Cell = self.queue.popleft()
            node_count += 1

            if isinstance(current_cell, Goal):
                print(f"\n<Node ({current_cell.x},{current_cell.y})> {node_count}")
                traversedPath = self.build_path(current_cell, self.path)
                print(traversedPath)
                return True

            for neighbor in [current_cell.north, current_cell.west, current_cell.south, current_cell.east]:
                if neighbor and neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.add(neighbor)
                    self.path.update({neighbor:current_cell})
        return False

    def build_path(self, goal_cell, path):
        traversedPath = []
        current_cell = goal_cell
        while current_cell != None:
            traversedPath.append(current_cell.get_coordinates())
            current_cell = path.get(current_cell)
        traversedPath.reverse()
        return traversedPath



        