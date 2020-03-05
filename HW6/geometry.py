from math import sqrt


class Figure:
    _name: str
    _angles: float

    def __init__(self, name: str, angles: float):
        self._name = name
        self._angles = angles

    def area(self):
        print(self._name + ' area is ' + str(self.get_area()))

    def perimeter(self):
        print(self._name + ' perimeter is ' + str(self.get_perimeter()))

    def get_perimeter(self):
        pass

    def get_area(self):
        pass

    def angles(self):
        print(self._name + " has " + str(self._angles) + " angles")
        return self._angles

    def add_square(self, figure):
        if not isinstance(figure, Figure):
            raise Exception('instance of figure class is required')
        sum_area = self.get_area() + figure.get_area()
        print(self._name + ' and ' + figure._name + ' sum area is ' + str(sum_area))
        return sum_area

    @property
    def name(self):
        return self._name


class Rectangle(Figure):
    _height: float
    _width: float

    def __init__(self, height: float, width: float):
        super().__init__('Rectangle', 4)
        self._height = height
        self._width = width

    def get_area(self):
        _area = self._height * self._width
        return _area

    def get_perimeter(self):
        _perimeter = 2 * (self._height + self._width)
        return _perimeter


class Square(Rectangle):

    def __init__(self, width: float):
        super().__init__(width=width, height=width)
        self._name = 'Square'


class Triangle(Figure):
    _side_a: float
    _side_b: float
    _side_c: float

    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__(name='Triangle', angles=3)
        self._side_c = side_c
        self._side_b = side_b
        self._side_a = side_a

    def get_perimeter(self):
        return self._side_a + self._side_b + self._side_c

    def get_area(self):
        p = self.get_perimeter() / 2
        return sqrt(p * (p - self._side_a) * (p - self._side_b) * (p - self._side_c))


class Circle(Figure):
    _radius: float

    def __init__(self, radius: float):
        super().__init__('Circle', 0)
        self._radius = radius

    def get_area(self):
        return 3.14 * self._radius * self._radius

    def get_perimeter(self):
        return 2 * 3.14 * self._radius


if __name__ == '__main__':
    rectangle = Rectangle(width=10, height=5)
    rectangle.angles()
    rectangle.area()
    rectangle.perimeter()

    # square = Square(width=10)
    # square.angles()
    # square.area()
    # square.perimeter()
    #
    # triangle = Triangle(side_a=10, side_b=10, side_c=10)
    # triangle.angles()
    # triangle.area()
    # triangle.perimeter()
    #
    # triangle.add_square(square)
    #
    # circle = Circle(radius=10)
    # circle.angles()
    # circle.area()
    # circle.perimeter()
    #
    # circle.add_square(triangle)
