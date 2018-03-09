class ShapeUI(object):

    def __init__(self, shape_reference):
        self.shape_reference = shape_reference

    def get_details(self):
        raise NotImplementedError("Subclass must implement abstract method.")


class CircleUI(ShapeUI):

    def get_details(self):
        command = input("Please enter a radius: ")
        if "." in command:
            self.shape_reference.shape.set_radius(float(command))
        else:
            self.shape_reference.shape.set_radius(int(command))


class QuadUI(ShapeUI):

    def get_details(self):
        command = input("Please enter a length: ")
        if "." in command:
            self.shape_reference.shape.set_length(float(command))
        else:
            self.shape_reference.shape.set_length(int(command))
        command = input("Please enter a width: ")
        if "." in command:
            self.shape_reference.shape.set_width(float(command))
        else:
            self.shape_reference.shape.set_width(int(command))


class PentagonUI(ShapeUI):

    def get_details(self):
        command = input("Please enter a side length: ")
        if "." in command:
            self.shape_reference.shape.set_side(float(command))
        else:
            self.shape_reference.shape.set_side(int(command))


class TriangleUI(ShapeUI):

    def get_details(self):
        command = input("Please enter a side length: ")
        if "." in command:
            self.shape_reference.shape.set_side(float(command))
        else:
            self.shape_reference.shape.set_side(int(command))

