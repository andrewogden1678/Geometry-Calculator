import math
from ui import *
from adapters import *


class Shape(object):

    def __init__(self, name):
        self.ui = None
        self.name = name

    def get_area(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    def get_perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    def get_shape_ui(self):
        return self.ui


class Circle(Shape):

    pi = math.pi

    def __init__(self, name, radius=1):
        super().__init__(name)
        self.radius = radius
        self.ui = CircleUI(TwoDAdapter(self))

    def get_area(self):
        return round(Circle.pi * self.radius ** 2, 2)

    def get_perimeter(self):
        return round(2 * Circle.pi * self.radius, 2)

    def set_radius(self, radius):
        self.radius = radius


class Quadrilateral(Shape):

    def __init__(self, name, length=1, width=1):
        super().__init__(name)
        self.length = length
        self.width = width
        self.ui = QuadUI(TwoDAdapter(self))

    def get_area(self):
        return round(self.length * self.width, 2)

    def get_perimeter(self):
        return round((2 * self.length) + (2 * self.width), 2)

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width


class Pentagon(Shape):

    def __init__(self, name, side=1):
        super().__init__(name)
        self.side = side
        self.ui = PentagonUI(TwoDAdapter(self))

    def get_area(self):
        return round((1 / 4) * (math.sqrt(5 * (5 + 2 * math.sqrt(5)))) * self.side ** 2, 2)

    def get_perimeter(self):
        return round(5 * self.side, 2)

    def set_side(self, side):
        self.side = side


class Triangle(Shape):

    def __init__(self, name, side=1):
        super().__init__(name)
        self.side = side
        self.ui = TriangleUI(TwoDAdapter(self))

    def get_area(self):
        return round((math.sqrt(3) / 4) * self.side**2, 2)

    def get_perimeter(self):
        return round(self.side * 3, 2)

    def set_side(self, side):
        self.side = side
