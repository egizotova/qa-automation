import pytest

from HW6.geometry import Triangle


def test_triangle_name():
    triangle = Triangle(side_a=10, side_b=10, side_c=10)
    assert triangle.name == 'Triangle'


def test_triangle_angles():
    triangle = Triangle(side_a=10, side_b=10, side_c=10)
    assert triangle.angles() == 3


def test_triangle_area():
    triangle = Triangle(side_a=10, side_b=10, side_c=10)
    assert triangle.area() < 100


def test_triangle_perimeter():
    triangle = Triangle(side_a=10, side_b=10, side_c=10)
    assert triangle.perimeter() == 30


def test_triangle_perimeter():
    triangle = Triangle(side_a=10, side_b=10, side_c=10)
    triangle2 = Triangle(side_a=10, side_b=10, side_c=10)
    assert triangle.add_square(triangle2) < 100


class NotFigure:
    some_value: str


def test_triangle_exception():
    try:
        triangle = Triangle(side_a=10, side_b=10, side_c=10)
        not_figure = NotFigure()
        triangle.add_square(not_figure)
        assert False
    except Exception:
        assert True


if __name__ == '__main__':
    test_triangle_exception()