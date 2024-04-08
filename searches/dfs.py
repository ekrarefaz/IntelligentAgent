""" Depth First Search """

from models.grid import Grid
from models.goal import Goal
from utils.build_path import build_path

class DFS:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.stack = []
        self.visited = set()
        self.path = {}

    """ Iterative DFS Search """
    def search(self):
        agent_start = self.grid.get_agent()
        self.stack.append(agent_start)
        node_count = 1

        while self.stack:
            current_cell = self.stack.pop()

            if current_cell not in self.visited:
                self.visited.add(current_cell)
                node_count += 1

                if isinstance(current_cell, Goal):
                    print(f"\n<Node ({current_cell.x},{current_cell.y})> {node_count}")
                    traversedPath = build_path(current_cell, self.path)
                    print(f"DFS Path : {traversedPath}")
                    return traversedPath, node_count

                for neighbor in [current_cell.north, current_cell.east, current_cell.south, current_cell.west]:
                    if neighbor != None and neighbor not in self.visited:
                        self.stack.append(neighbor)
                        self.path[neighbor] = current_cell
        print(f"No goal reachable <{node_count}>")
        return None, node_count
