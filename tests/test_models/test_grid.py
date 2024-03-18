from models.grid import Grid
from models.agent import Agent
from models.goal import Goal
from models.wall import Wall
from models.cell import Cell

""" Initialize Grid """
def init():
   return Grid(5, 6)

""" Test Grid Initialization """
def test_grid_initialization():
    grid = init()
    
    assert len(grid._grid) == 5
    for row in grid._grid:
        assert len(row) == 6

""" Test Agent Getter """
def test_agent_getter():
    grid = init()

    assert grid.get_agent() == None

""" Test Wrong Agent Setter"""
def test_agent_setter_out_of_bounds():
    grid = init()

    grid.set_agent(7,7)
    assert grid.get_agent() != Agent(7,7)
    assert grid.get_agent() == None

""" Test Correct Agent Setter"""
def test_agent_setter_within_bounds():
    grid = init()

    grid.set_agent(1,1)
    assert grid.get_agent() == grid._grid[1][1]

""" Test Add Goal to Grid """
def test_goal_addition():
    grid = init()

    assert grid._goal == []
    grid.add_goal(2,0)
    assert isinstance(grid._grid[0][2], Goal) == True

""" Test Wall Addition Within Bounds """
def test_wall_addition_within_bounds():
    grid = init()

    assert isinstance(grid._grid[0][0], Cell)
    grid.add_wall(0,0,2,2)
    assert isinstance(grid._grid[0][0], Wall)

""" Test Wall Addition Outof Bounds """
def test_wall_addition_out_of_bounds():
    grid = init()

    grid.add_wall(5, 4, 3, 3)
    assert isinstance(grid._grid[4][5], Wall)

    