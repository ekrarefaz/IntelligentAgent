from models.wall import Wall

""" Initialize Wall """
def init():
    return Wall(0, 0, 5, 6)

""" Test Setter & Getter """
def test_dimension_getter():
    wall = init()

    assert wall.height == 6
    assert wall.width == 5

""" Test Print Symbol """
def test_print_symbol():
    wall = init()

    assert wall.print_symbol() == " W "
