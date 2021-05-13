from figuraGeometrica import GeometricFigure
from color import Color


class Square(GeometricFigure, Color):
    def __init__(self, side, color):
        GeometricFigure.__init__(self, side, side)
        Color.__init__(self, color)
        #super().__init__(side, side)

    def area(self):
        return self.get_width() * self.get_high()

    def __str__(self):
        return GeometricFigure.__str__(self) + " Color: " + self.get_color()