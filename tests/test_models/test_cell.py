from models.cell import Cell
import pytest

""" Testing Cell Initialization """
def test_init():
    cell = Cell(10,20)
    assert cell.x == 10
    assert cell.y == 20
    for neighbor in ["north", "south", "east", "west"]:
        assert cell.neighbor == None

""" Testing Coordinates Method """
def test_get_coordinate():
    cell = Cell(11, 12)
    assert cell.get_coordinates == (11,12)