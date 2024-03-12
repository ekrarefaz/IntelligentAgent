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

    """ Set pointers for neighboring cells """
    grid.set_neighbors()

    return grid



def main():
    grid_size, agent_position, goal_positions, wall_positions = parser()
    grid = grid_init(grid_size, agent_position, goal_positions, wall_positions)

    #DEBUG
    print("grid created")
    grid.print_grid()


main()