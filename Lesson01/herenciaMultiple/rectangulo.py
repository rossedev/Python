from figuraGeometrica import GeometricFigure
from color import Color

class Rectangle(GeometricFigure, Color):
    def __init__(self,width, high, color):
        GeometricFigure.__init__(self, width, high)
        Color.__init__(self, color)

    def area(self):
        return self.get_width() * self.get_high()

    def __str__(self):
        return GeometricFigure.__str__(self) + " Color: " + self.get_color()