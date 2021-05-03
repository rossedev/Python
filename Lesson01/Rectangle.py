class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


baseInput = int(input('Provides the base: '))
heightInput = int(input('Provides the height: '))

rectangle = Rectangle(baseInput, heightInput)
print("The area is:", rectangle.area())
