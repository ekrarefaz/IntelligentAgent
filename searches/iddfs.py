from collections import deque
from models.cell import Cell
from models.grid import Grid
from models.goal import Goal
from utils.build_path import build_path

class IDDFS:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.queue = deque()
        self.visited = set()
        self.path = {}
    
    def dls(self, cell: Cell, depth, limit):
        current_cell = cell

        if depth > limit:
            return False
        self.visited.add(current_cell)
        
        if isinstance(current_cell, Goal):
            return current_cell
        
        for neighbor in [current_cell.north, current_cell.east, current_cell.south, current_cell.west]:
            if neighbor and neighbor not in self.visited:
                result = self.dls(neighbor, depth + 1, limit)
                if result: 
                    self.path[neighbor] = cell 
                    return result
        return None
    
    def search(self):
        limit = 0
        start_agent = self.grid.get_agent()

        while True:
            self.visited.clear()
            self.path.clear()
            goal_cell = self.dls(start_agent, 0, limit)

            if goal_cell:
                print(f"\n<Node ({goal_cell.x},{goal_cell.y})>")
                traversedPath = build_path(goal_cell, self.path)
                print(f"IDDFS Path : {traversedPath}")
                return traversedPath
            limit += 1
        return None