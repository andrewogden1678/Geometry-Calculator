import shapes
import tridshapes
import sys


class Program(object):

    def run(self, new_shapes):
        while 1:
            command = input("Please enter a shape (cube, triangular pyramid, circle, quadrilateral, pentagon or triangle). Type 'exit' to quit the program: ")

            for shape in new_shapes:
                if command in shape.name:
                    shape.get_shape_ui().get_details()
                    print("Area/Volume: ", shape.algorithm1(), "\nPerimeter/Surface area: ", shape.algorithm2())
                elif "exit" in command:
                    sys.exit("Seeya!")


SHAPES = [shapes.TwoDAdapter(shapes.Circle("circle")),
          shapes.TwoDAdapter(shapes.Quadrilateral("quadrilateral")),
          shapes.TwoDAdapter(shapes.Pentagon("pentagon")),
          shapes.TwoDAdapter(shapes.Triangle("triangle")),
          tridshapes.TriDAdapter(tridshapes.RectangularPrism('cube')),
          tridshapes.TriDAdapter(tridshapes.TriPyramid('triangular pyramid'))]

program = Program()

program.run(SHAPES)
