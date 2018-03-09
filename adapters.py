class Adapter(object):

    def __init__(self, shape):
        self.shape = shape
        self.name = shape.name

    def get_shape_ui(self):
        return self.shape.ui

    def algorithm1(self):
        raise NotImplementedError("Subclass must implement abstract method.")

    def algorithm2(self):
        raise NotImplementedError("Subclass must implement abstract method.")


class TriDAdapter(Adapter):

    def algorithm1(self):
        return self.shape.get_volume()

    def algorithm2(self):
        return self.shape.get_surface_area()


class TwoDAdapter(Adapter):

    def algorithm1(self):
        return self.shape.get_area()

    def algorithm2(self):
        return self.shape.get_perimeter()