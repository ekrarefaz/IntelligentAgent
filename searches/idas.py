from models.grid import Grid
from models.cell import Cell
from models.goal import Goal
from utils.build_path import build_path

class IDAS:
    """
    Initialize the IDAS search with the grid.
    """
    def __init__(self, grid: Grid):
        self.grid = grid
        self.goals = self.grid._goal
        self.visited = set()
        self.path = {}
        self.node_count = 0

    """
    Manhattan Distance method for calculating heuristic
    """
    def manhattan_distance(self, cell: Cell, goal: Goal):
        return abs(cell.x - goal.x) + abs(cell.y - goal.y)

    """
    When all else equal explore directional bias
    """
    def directional_bias(self, cell: Cell, neighbor: Cell):
        bias = {'UP': 0, 'LEFT': 1, 'DOWN': 2, 'RIGHT': 3}
        direction = self.grid.get_direction(cell, neighbor)
        return bias.get(direction)

    """
    Heuristic calculation
    """
    def heuristic(self, cell: Cell):
        return min(self.manhattan_distance(cell, goal) for goal in self.grid._goal)
    
    """ 
    Calculate f(n) for priority exploration
    """
    def calculate_f(self, cell: Cell, parent: Cell = None) -> int:

        if parent == None:
            cell.g = 0
        else:
            cell.g = parent.g + 1

        h = self.heuristic(cell)
        return cell.g + h
    
    """
    Perform the IDAS search to find a path to the goal.
    """
    def search(self):
        self.node_count = 0        
        agent_start = self.grid.get_agent()
        threshold = self.calculate_f(agent_start)
        self.min_threshold = float('inf')

        while True:
            self.visited = set()  # Reset visited each iteration
            temp = self.search_recursive(agent_start, 0, threshold, None)
            if temp == float('inf'):
                print(f"No goal reachable; {self.node_count}")
                return None, self.node_count
            elif isinstance(temp, tuple):
                """
                Check if the search has reached the goal. If so, build the path and return.
                """
                current_cell = temp[0]
                print(f"\n<Node ({current_cell.x},{current_cell.y})> {self.node_count}")
                traversedPath = build_path(current_cell, self.path)
                print(f"IDAS Path : {traversedPath}")
                return traversedPath, self.node_count
            
            threshold = temp

    """
    Recursively search for the goal using a depth-first approach with a threshold.
    """
    def search_recursive(self, cell: Cell, g: int, threshold: int, parent: Cell):
        f = self.calculate_f(cell, parent)
        if f > threshold:
            return f
        if cell in self.visited:
            return self.min_threshold
        self.visited.add(cell)
        self.path[cell] = parent
        self.node_count += 1

        if isinstance(cell, Goal):
            return (cell, g)
        min_threshold = float('inf')

        """
        Explore univisted neighbors recursively to find the goal.
        """
        for neighbor in [cell.north, cell.east, cell.south, cell.west]:
            if neighbor is not None and neighbor not in self.visited:
                temp = self.search_recursive(neighbor, g + 1, threshold, cell)
                if isinstance(temp, tuple):
                    return temp 
                if temp < min_threshold:
                    min_threshold = temp

        self.visited.remove(cell)
        return min_threshold


