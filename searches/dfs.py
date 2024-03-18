from models.grid import Grid
from models.goal import Goal

class DFS:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.stack = []
        self.visited = set()
        self.path = {}

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
                    traversedPath = self.build_path(current_cell, self.path)
                    print(traversedPath)
                    return True

                for neighbor in [current_cell.north, current_cell.east, current_cell.south, current_cell.west]:
                    if neighbor != None and neighbor not in self.visited:
                        self.stack.append(neighbor)
                        self.path[neighbor] = current_cell

    def build_path(self, goal_cell, path):
        traversedPath = []
        current_cell = goal_cell
        while current_cell != None:
            traversedPath.append(current_cell.get_coordinates())
            current_cell = path.get(current_cell)
        traversedPath.reverse()
        return traversedPath