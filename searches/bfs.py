""" Breadth First Search """

from models.grid import Grid
from models.cell import Cell
from models.goal import Goal
from collections import deque

from utils.build_path import build_path

class BFS:

    def __init__(self, grid: Grid):
        self.grid = grid
        self.queue = deque()
        self.visited = set()
        self.path = {}

    """ BFS Search """
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
                traversedPath = build_path(current_cell, self.path)
                print(f"BFS Path : {traversedPath}")
                return traversedPath, node_count

            for neighbor in [current_cell.north, current_cell.west, current_cell.south, current_cell.east]:
                if neighbor and neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.add(neighbor)
                    self.path[neighbor] = current_cell
        return



        