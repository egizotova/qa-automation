from HW6.geometry import Circle


def test_circle_name():
    circle = Circle(radius=3)
    assert circle.name == 'Circle'


def test_circle_angles():
    circle = Circle(radius=3)
    assert circle.angles() == 0


def test_circle_area():
    circle = Circle(radius=3)
    assert circle.area() > 6


def test_circle_perimeter():
    circle = Circle(radius=3)
    assert circle.perimeter() > 10

def test_circle_perimeter():
    circle = Circle(radius=3)
    circle2 = Circle(radius=1)
    assert circle.add_square(circle2) < 100


class NotFigure:
    some_value: str


def test_circle_exception():
    try:
        circle = Circle(radius=3)
        not_figure = NotFigure()
        circle.add_circle(not_figure)
        assert False
    except Exception:
        assert True


if __name__ == '__main__':
    test_circle_exception()