import argparse
import csv
import json
import os

from searches.bfs import BFS
from searches.dfs import DFS
from searches.gbfs import GBFS
from searches.a_star import AS
from searches.iddfs import IDDFS

from models.grid import Grid
from utils.data_parser import gridparser
from performance_test.test_runner import run_test
from utils.grid_init import grid_init

def log_result(results):
    fieldnames = ['algorithm', 'execution_time', 'peak_memory_usage', 'nodes_explored', 'path_length']
    with open('results.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
def load_grid_files(folder_path='grid_configs'):
    return [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.txt')]

def main():
    parser = argparse.ArgumentParser(description="Run search algorithms on specified grids.")
    parser.add_argument('--grid', type=str, help="Path to the grid configuration file.")
    parser.add_argument('--grid-all', action='store_true', help="Run the specified algorithm on all grids in the grid_configs folder.")
    parser.add_argument('--algorithm', type=str, help="Specify the algorithm to test.")
    parser.add_argument('--algorithm-all', action='store_true', help="Test all algorithms for the specified grid.")

    args = parser.parse_args()
    results = []
    algorithm_map = {
        'BFS': BFS,
        'DFS': DFS,
        'GBFS': GBFS,
        'AStar': AS,
        'IDDFS': IDDFS
    }

    if args.grid_all:
        grid_files = load_grid_files()
    elif args.grid:
        grid_files = [args.grid]
    else:
        print("Please specify a grid with --grid or use --grid-all to run all grids.")
        return

    if args.algorithm_all:
        algorithms_to_run = list(algorithm_map.values())
    elif args.algorithm in algorithm_map:
        algorithms_to_run = [algorithm_map[args.algorithm]]
    else:
        print("Please specify an algorithm with --algorithm or use --algorithm-all to test all.")
        return

    for grid_file in grid_files:
        grid_size, agent_position, goal_positions, wall_positions = gridparser(grid_file) 
        grid = grid_init(grid_size, agent_position, goal_positions, wall_positions)

        for algorithm in algorithms_to_run:
            result = run_test(algorithm, grid)  
            print(f"Results for {grid_file} using {algorithm.__name__}: {results}")
            results.append(result)
            log_result(results)

if __name__ == "__main__":
    main()
