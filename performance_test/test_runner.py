import time
import tracemalloc

from searches.bfs import BFS
from searches.dfs import DFS
from searches.gbfs import GBFS
from searches.a_star import AS
from searches.iddfs import IDDFS

from models.grid import Grid

def run_test(algorithm_class, grid: Grid):
    algorithm = algorithm_class(grid)

    start_time = time.time()
    tracemalloc.start()

    path, nodes_explored = algorithm.search()

    execution_time = time.time() - start_time
    _, peak_memory_usage = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    if path != None:
        path_length = len(path)
    else:
        path_length = 0

    results = {
        'algorithm': algorithm_class.__name__,
        'execution_time': execution_time,
        'peak_memory_usage': peak_memory_usage,
        'nodes_explored': nodes_explored,
        'path_length': path_length
    }
    return results
