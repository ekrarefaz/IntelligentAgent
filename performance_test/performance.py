import argparse
import csv
import json
import os

from searches.bfs import BFS
from searches.dfs import DFS
from searches.gbfs import GBFS
from searches.a_star import AS
from searches.idas import IDAS
from searches.iddfs import IDDFS

from models.grid import Grid
from utils.data_parser import gridparser
from performance_test.test_runner import run_test
from utils.grid_init import grid_init
from visualizations.visual import visualize

"""
Logging performance results in CSV file
"""
def log_result(results):
    fieldnames = ['algorithm', 'execution_time', 'peak_memory_usage', 'nodes_explored', 'path_length']
    with open('results.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
"""
Performance testing for all search algorithms against specified grid file
"""
def performance(gridfile):
    results = []
    """
    Dictionary mapping of search algorithms
    """
    algorithm_map = {
        'BFS': BFS,
        'DFS': DFS,
        'GBFS': GBFS,
        'AS': AS,
        'IDDFS': IDDFS,
        'IDAS': IDAS
    }
    
    """
    Create grid from grid file
    """
    grid_size, agent_position, goal_positions, wall_positions = gridparser(gridfile) 
    grid = grid_init(grid_size, agent_position, goal_positions, wall_positions)

    """
    Run performance tests on all search algorithms
    """
    for algorithm in algorithm_map.values():
        print(f"Running {algorithm.__name__} on {gridfile}")
        result = run_test(algorithm, grid)  
        results.append(result)
        log_result(results)

    """
    Visualize the performance results using MatplotLib
    """
    visualize()

