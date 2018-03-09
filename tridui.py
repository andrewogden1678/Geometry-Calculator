class TriDShapeUI(object):

    def __init__(self, shape_reference):
        self.shape_reference = shape_reference

    def get_details(self):
        raise NotImplementedError("Subclass must implement abstract method.")


class CubeUI(TriDShapeUI):

    def get_details(self):
        command = input('Please enter a length: ')
        if "." in command:
            self.shape_reference.shape.set_length(float(command))
        else:
            self.shape_reference.shape.set_length(int(command))

        command = input('Please enter a width: ')
        if "." in command:
            self.shape_reference.shape.set_width(float(command))
        else:
            self.shape_reference.shape.set_width(int(command))

        command = input('Please enter a height: ')
        if "." in command:
            self.shape_reference.shape.set_height(float(command))
        else:
            self.shape_reference.shape.set_height(int(command))


class TriPyramidUI(TriDShapeUI):

    def get_details(self):
        command = input('Please enter a base length: ')
        if "." in command:
            self.shape_reference.shape.set_length(float(command))
        else:
            self.shape_reference.shape.set_length(int(command))

        command = input('Please enter a base width: ')
        if "." in command:
            self.shape_reference.shape.set_width(float(command))
        else:
            self.shape_reference.shape.set_width(int(command))

        command = input('Please enter a pyramid height: ')
        if "." in command:
            self.shape_reference.shape.set_height(float(command))
        else:
            self.shape_reference.shape.set_height(int(command))

