from models.grid import Grid
from models.cell import Cell
from models.goal import Goal

from utils.build_path import build_path
class IDDFS:
    def __init__(self, grid):
        self.grid = grid
        self.visited = set()
        self.path = {}
    
    def search(self):
        limit = 0
        agent_start = self.grid.get_agent()
        prev_visited = 0
        max_depth = -1

        while True:
            """Use a stack for the nodes to explore, each entry is a tuple (cell, depth, parent)"""
            stack = [(agent_start, 0, None)]
            """ Reset the visited and path dictionaries """
            self.visited.clear()
            self.path.clear()
            node_count = 1
            current_max_depth = 0

            while stack:
                current_cell, depth, parent = stack.pop()
                if current_cell in self.visited:
                    continue

                node_count += 1
                self.visited.add(current_cell)
                self.path[current_cell] = parent
                """
                Check for goal, if goal build path and return
                """
                if isinstance(current_cell, Goal):
                    print(f"\n<Node ({current_cell.x},{current_cell.y})> {node_count}")
                    traversedPath = build_path(current_cell, self.path)
                    print(f"IDDFS Path : {traversedPath}")
                    return traversedPath, node_count
                
                current_max_depth = max(current_max_depth, depth)
                """
                Explore and add neighbors to the stack if they haven't
                been visited if the depth limit hasn't been reached.
                """
                if depth < limit:
                    for neighbor in [current_cell.north, current_cell.east, current_cell.south, current_cell.west]:
                        if neighbor and neighbor not in self.visited:
                            stack.append((neighbor, depth + 1, current_cell))
            """
            If the depth is the same as the previous iteration,
            then no goal is reachable.
            """
            if max_depth == current_max_depth:
                print(f"No goal reachable <{node_count}>")
                return None, node_count
            
            """
            Increase the depth limit and try again
            """
            max_depth = current_max_depth
            limit += 2

    """
    IDDFS Extension to handle multiple goals
    """
    def search_extension(self):
        limit = 0
        agent_start = self.grid.get_agent()
        max_depth = -1
        paths_to_goals = {}

        while True:
            """Use a stack for the nodes to explore, each entry is a tuple (cell, depth, parent)"""
            stack = [(agent_start, 0, None)]
            """ Reset the visited and path dictionaries """
            self.visited.clear()
            self.path.clear()
            node_count = 1
            current_max_depth = 0

            while stack:
                current_cell, depth, parent = stack.pop()
                if current_cell in self.visited:
                    continue

                node_count += 1
                self.visited.add(current_cell)
                self.path[current_cell] = parent
                """
                Check for goal, if goal build path and return
                """
                if isinstance(current_cell, Goal):
                    paths_to_goals[(current_cell.x, current_cell.y)] = build_path(current_cell, self.path)
                    print(f"\n<Node ({current_cell.x},{current_cell.y})> {node_count}")
                    if len(paths_to_goals) == len(self.grid._goal):
                        print(f"All goals reached.")
                        for goal, path in paths_to_goals.items():
                            print(f"IDDFS Path to {goal}: {path}")
                        return paths_to_goals, node_count
                
                current_max_depth = max(current_max_depth, depth)
                """
                Explore and add neighbors to the stack if they haven't
                been visited if the depth limit hasn't been reached.
                """
                if depth < limit:
                    for neighbor in [current_cell.north, current_cell.east, current_cell.south, current_cell.west]:
                        if neighbor and neighbor not in self.visited:
                            stack.append((neighbor, depth + 1, current_cell))
            """
            If the depth is the same as the previous iteration,
            then no goal is reachable.
            """
            if max_depth == current_max_depth:
                print(f"No goal reachable <{node_count}>")
                return None, node_count
            
            """
            Increase the depth limit and try again
            """
            max_depth = current_max_depth
            limit += 2

        