def gridparser(filename):
    """ open the file for reading """
    file = open(filename, "r")
    lines = file.readlines()

    grid_size = None
    agent_position = None
    goal_positions = []
    wall_positions = []

    """ Read and process data line by line from the text file """
    for count, line in enumerate(lines):
        if count == 0:
            """ read the grid size """
            grid_size = tuple(map(int,line.strip().strip("[]").split(",")))
        elif count == 1:
            """ read the agent coordinates """
            agent_position = tuple(map(int, line.strip().strip("()").split(",")))
        elif count == 2:
            """ read the goal coordinates using loop """
            goals = line.strip().split("|")
            for goal in goals:
                goal_positions.append(tuple(map(int, goal.strip().strip("()").split(","))))
        else:
            """ read the wall specs using loop """
            walls = line.strip().split("|")
            for wall in walls:
                wall_positions.append(tuple(map(int, wall.strip().strip("()").split(","))))
    
    file.close()
    return grid_size, agent_position, goal_positions, wall_positions