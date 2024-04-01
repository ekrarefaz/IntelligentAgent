import sys
from utils.data_parser import gridparser
from models.cell import Cell
from models.grid import Grid
from searches.bfs import BFS
from searches.dfs import DFS
from searches.gbfs import GBFS
from searches.a_star import AS
from searches.iddfs import IDDFS
from utils.grid_init import grid_init

def dfs(grid: Grid):
    search_agent = DFS(grid)
    search_agent.search()

def bfs(grid: Grid):
    search_agent = BFS(grid)
    search_agent.search()

def gbfs(grid: Grid):
    search_agent = GBFS(grid)
    search_agent.search()

def astar(grid: Grid):
    search_agent = AS(grid)
    search_agent.search()

def iddfs(grid: Grid):
    search_agent = IDDFS(grid)
    search_agent.search()

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 [FILENAME.py] [METHOD]")
        sys.exit(1)
    
    method = sys.argv[2].lower() 
    grid_size, agent_position, goal_positions, wall_positions = gridparser(sys.argv[1])

    grid = grid_init(grid_size, agent_position, goal_positions, wall_positions)

    search_methods = {
        'bfs': bfs,
        'dfs': dfs,
        'gbfs': gbfs,
        'astar': astar,
        'iddfs': iddfs
    }

    search_function = search_methods.get(method)
    if search_function:
        print(f"Executing {method.upper()} search...")
        search_function(grid)
    else:
        print(f"Search method '{method}' not recognized. Available methods are: {', '.join(search_methods.keys())}")
        sys.exit(1)

if __name__ == "__main__":
    main()
