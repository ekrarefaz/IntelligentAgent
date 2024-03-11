from utils.data_parser import parser
from models.cell import Cell
from models.grid import Grid

def grid_init(grid_size, agent_position, goal_positions, wall_positions):

    """ Initialize the grid with Data from data parser """
    grid = Grid(*grid_size)

    """ Initialize the agent in the grid """
    grid.set_agent(*agent_position)

    """ Initialize the goals in the grid """
    for goal in goal_positions:
        grid.add_goal(*goal)

    """ Initialize the walls in the grid """
    for wall in wall_positions:
        grid.add_wall(*wall)

    return grid

""" set pointers for neighb
oring cells by direction"""
def set_neighbors(grid: Grid, grid_size):
    x_cell_count, y_cell_count = grid_size

    """ iterate over each cell in the grid by grid[column][row] """
    column_index = 0
    while (column_index < x_cell_count):
        row_index = 0

        while (row_index < y_cell_count):

            """ set pointers for north """
            if row_index > 0:
                grid.grid[column_index][row_index].north = grid.grid[column_index][row_index - 1]
            else:
                grid.grid[column_index][row_index].north = None
            
            """ set pointers for south """
            if row_index < y_cell_count - 1:
                grid.grid[column_index][row_index].south = grid.grid[column_index][row_index + 1]
            else:
                grid.grid[column_index][row_index].south = None

            """ set pointers for west """
            if column_index > 0:
                grid.grid[column_index][row_index].west = grid.grid[column_index - 1][row_index]
            else:
                grid.grid[column_index][row_index].west = None

            """ set pointers for east """
            if column_index > 0:
                grid.grid[column_index][row_index].east = grid.grid[column_index + 1][row_index]
            else:
                grid.grid[column_index][row_index].east = None

def main():
    grid_size, agent_position, goal_positions, wall_positions = parser()
    
    grid = grid_init(grid_size, agent_position, goal_positions, wall_positions)
    #DEBUG
    print("grid created")

    set_neighbors(grid, grid_size)
    #DEBUG
    print("neighbors created")

main()