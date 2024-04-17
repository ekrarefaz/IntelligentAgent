import sys
import argparse
from utils.data_parser import gridparser
from performance_test.performance import performance
from models.cell import Cell
from models.grid import Grid
from searches.bfs import BFS
from searches.dfs import DFS
from searches.gbfs import GBFS
from searches.a_star import AS
from searches.iddfs import IDDFS
from searches.idas import IDAS
from utils.grid_init import grid_init

"""
Search Algorithms
"""
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

def idas(grid: Grid):
    search_agent = IDAS(grid)
    search_agent.search()

def main():
    """
    Search methods dictionary
    """
    search_methods = {
        'BFS': bfs,
        'DFS': dfs,
        'GBFS': gbfs,
        'AS': astar,
        'IDDFS': iddfs,
        'IDAS' : idas
    }
    """
    General CLI Argument Parser
    """
    parser = argparse.ArgumentParser(description="Run Search Algorithms on Grids")
    parser.add_argument('filename', type=str, help="Path to the grid configuration file.")
    parser.add_argument('-m', '-method', type=str, help="Search method to use. i.e. BFS, DFS, GBFS, AS, IDDFS, IDAS")
    """
    Performance Testing Argument Parser
    """
    parser.add_argument('-p', '--performance', action='store_true', help="Run performance tests on all search algorithms.")

    args = parser.parse_args()
    gridfile = args.filename
    method = args.m

    """
    Parse the grid file and initialize the grid
    """
    grid_size, agent_position, goal_positions, wall_positions = gridparser(gridfile)
    grid = grid_init(grid_size, agent_position, goal_positions, wall_positions)

    if args.performance:
        print("Running performance tests...")
        performance(gridfile)
    """
    Execute the search method
    """
    search_function = search_methods.get(method)
    if search_function:
        print(f"Executing {method.upper()} search...")
        search_function(grid)
    else:
        print(f"Search method '{method}' not recognized. Available methods are: {', '.join(search_methods.keys())}")
        sys.exit(1)

if __name__ == "__main__":
    main()
