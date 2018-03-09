from tridui import *
from adapters import *


class TriDShape(object):

    def __init__(self, name):
        self.ui = None
        self.name = name
        self.side_num = 0

    def get_volume(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    def get_surface_area(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    def get_shape_ui(self):
        return self.ui


class RectangularPrism(TriDShape):

    def __init__(self, name, length=1, width=1, height=1):
        super().__init__(name)
        self.side_num = 6
        self.ui = CubeUI(TriDAdapter(self))
        self.length = length
        self.width = width
        self.height = height

    def get_volume(self):
        return round(self.length * self.width * self.height, 2)

    def get_surface_area(self):
        return round((self.width * self.height) * 6, 2)

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


class TriPyramid(TriDShape):

    def __init__(self, name, length=1, width=1, height=1):
        super().__init__(name)
        self.side_num = 5
        self.ui = TriPyramidUI(TriDAdapter(self))
        self.length = length
        self.width = width
        self.height = height

    def get_volume(self):
        return round((1 / 3) * (self.length * self.width) * self.height, 2)

    def get_surface_area(self):
        return round((self.width * self.height) * 5, 2)

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
