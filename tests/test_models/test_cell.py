from models.cell import Cell

""" Cell Initialization """
def init(x=11,y=22):
    return Cell(x,y)

""" Test Cell Initialization """
def test_init():
    cell = init()

    assert cell.x == 11
    assert cell.y == 22

""" Test Cell Neighbor Getter & Setter """
def test_neighbors():
    cell = init()

    assert cell.north == None
    assert cell.south == None
    assert cell.east == None
    assert cell.west == None

    north_cell = init(100,200)
    cell.north = north_cell
    assert cell.north == north_cell

""" Test Coordinates Method """
def test_get_coordinate():
    cell = init()

    cell.get_coordinates() == (11, 22)

""" Test Print Method """
def test_print_symbol():
    cell = init()

    cell.print_symbol() == " . "