def build_path(goal_cell, path):
    traversedPath = []
    current_cell = goal_cell
    while current_cell != None:
        traversedPath.append(current_cell.get_coordinates())
        current_cell = path.get(current_cell)
    traversedPath.reverse()
    return traversedPath