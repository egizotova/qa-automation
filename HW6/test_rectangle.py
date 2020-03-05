from HW6.geometry import Rectangle


def test_rectangle_name():
    rectangle = Rectangle(height=2, width=3)
    assert rectangle.name == 'Rectangle'


def test_rectangle_angles():
    rectangle = Rectangle(height=2, width=3)
    assert rectangle.angles() == 4


def test_rectangle_area():
    rectangle = Rectangle(height=2, width=3)
    assert rectangle.area() == 6


def test_rectangle_perimeter():
    rectangle = Rectangle(height=2, width=3)
    assert rectangle.perimeter() == 10

def test_rectangle_perimeter():
    rectangle = Rectangle(height=2, width=3)
    rectangle2 = Rectangle(height=3, width=4)
    assert rectangle.add_square(rectangle2) < 100


class NotFigure:
    some_value: str


def test_triangle_exception():
    try:
        rectangle = Rectangle(height=3, width=4)
        not_figure = NotFigure()
        rectangle.add_square(not_figure)
        assert False
    except Exception:
        assert True


if __name__ == '__main__':
    test_rectangle_exception()