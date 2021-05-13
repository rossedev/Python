from cuadrado import Square
from rectangulo import Rectangle

square = Square(2, "Black")
rectangle = Rectangle(4, 5, "Green")

print("Square", square)
print("Area square", square.area())
print("Rectangle", rectangle)
print("Area rectangle", rectangle.area())

#metodo para saber el orden de los metodos
print(Square.mro())