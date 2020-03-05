from HW6.geometry import Square


def test_square_name():
    square = Square(width=3)
    assert square.name == 'Square'


def test_rsquare_angles():
    square = Square(width=3)
    assert square.angles() == 4


def test_square_area():
    square = Square(width=3)
    assert square.area() == 9


def test_square_perimeter():
    square = Square(width=3)
    assert square.perimeter() == 12

def test_rectangle_perimeter():
    square = Square(width=3)
    square2 = Square(width=4)
    assert square.add_square(square2) < 100


class NotFigure:
    some_value: str


def test_square_exception():
    try:
        square = Square(width=4)
        not_figure = NotFigure()
        square.add_square(not_figure)
        assert False
    except Exception:
        assert True


if __name__ == '__main__':
    test_square_exception()