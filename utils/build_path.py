"""
Builds the path from the start cell to the goal cell using the path dictionary
"""
def build_path(goal_cell, path):
    traversedPath = []
    current_cell = goal_cell
    """
    Traverse the path dictionary to build the path
    """
    while current_cell != None:
        traversedPath.append(current_cell.get_coordinates())
        current_cell = path.get(current_cell)
    traversedPath.reverse()
    return traversedPath