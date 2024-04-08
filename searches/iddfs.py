from models.grid import Grid
from models.cell import Cell
from models.goal import Goal

from utils.build_path import build_path
class IDDFS:
    """ Initialize """
    def __init__(self, grid: Grid):
        self.grid = grid
        self.visited = set()
        self.path = {}
    
    """ perform depth limited DFS """
    def dls(self, cell: Cell, depth, limit, node_count):
        if depth > limit:
            return None, node_count
        
        self.visited.add(cell)
        node_count += 1

        if isinstance(cell, Goal):
            return cell, node_count
        
        # recursively explore each unvisited neighbor
        for neighbor in [cell.north, cell.east, cell.south, cell.west]:
            if neighbor and neighbor not in self.visited:
                result, node_count = self.dls(neighbor, depth + 1, limit, node_count)
                if result:
                    self.path[neighbor] = cell
                    return result, node_count
        return None, node_count
    
    """ iteratively increase the depth limit and call dls() """
    def search(self):
        limit = 0
        node_count = 0
        prev_visited_count = 0

        while True:
            # clear visited and path for each increment in depth for fresh start
            self.visited.clear()
            self.path.clear()
            goal_cell, node_count = self.dls(self.grid.get_agent(), 0, limit, node_count)

            # if goal cell is found, build the path and return
            if goal_cell:
                print(f"\n<Node ({goal_cell.x},{goal_cell.y})> {node_count}")
                traversedPath = build_path(goal_cell, self.path)
                print(f"IDDFS Path : {traversedPath}")
                return traversedPath, node_count

            # Check if no new nodes were visited in this iteration
            if len(self.visited) == prev_visited_count:
                print("Goal not reachable.")
                return None, node_count

            prev_visited_count = len(self.visited)
            limit += 1

