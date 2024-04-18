""" Breadth First Search """

from models.grid import Grid
from models.cell import Cell
from models.goal import Goal
from collections import deque

from utils.build_path import build_path

class BFS:
    """
    Initialize the BFS Search with the grid.
    """
    def __init__(self, grid: Grid):
        self.grid = grid
        self.queue = deque()
        self.visited = set()
        self.path = {}
        self.goals = self.grid._goal

    """
    BFS Search
    """
    def search(self):
        agent_start: Cell = self.grid.get_agent()
        self.queue.append(agent_start)
        self.visited.add(agent_start)
        node_count = 1

        while self.queue:
            current_cell: Cell = self.queue.popleft()
            node_count += 1
            """
            Check if the current cell is a goal, if so build the path and return
            """
            if isinstance(current_cell, Goal):
                print(f"\n<Node ({current_cell.x},{current_cell.y})> {node_count}")
                traversedPath = build_path(current_cell, self.path)
                print(f"BFS Path : {traversedPath}")
                return traversedPath, node_count
            """
            Explore each unvisited neighbor and add to the queue
            """
            for neighbor in [current_cell.north, current_cell.west, current_cell.south, current_cell.east]:
                if neighbor and neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.add(neighbor)
                    self.path[neighbor] = current_cell
        print(f"No goal reachable <{node_count}>")
        return None, node_count

    """
    BFS Extension to handle multiple goals
    """
    def search_extension(self):
        agent_start: Cell = self.grid.get_agent()
        self.queue.append(agent_start)
        self.visited.add(agent_start)
        node_count = 1
        paths_to_goals = {}

        while self.queue:
            current_cell: Cell = self.queue.popleft()
            node_count += 1
            """
            Extended implementation of BFS to handle multiple goals. Using a goal counter
            to keep track of the number of goals visited. If goal count is equal to the total
            number of goals, return the path.
            """
            if isinstance(current_cell, Goal):
                paths_to_goals[(current_cell.x, current_cell.y)] = build_path(current_cell, self.path)
                print(f"\n<Node ({current_cell.x},{current_cell.y})> {node_count}")
                if len(paths_to_goals) == len(self.goals):
                    print(f"All goals reached.")
                    for goal, path in paths_to_goals.items():
                        print(f"DFS Path to {goal} : {path}")
                    return paths_to_goals, node_count
            """
            Explore each unvisited neighbor and add to the queue
            """
            for neighbor in [current_cell.north, current_cell.west, current_cell.south, current_cell.east]:
                if neighbor and neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.add(neighbor)
                    self.path[neighbor] = current_cell
        print(f"No goal reachable <{node_count}>")
        return None, node_count




        