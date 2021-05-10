class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "Color is:" + self.color + " and wheels: " + str(self.wheels)

class Car(Vehicle):
    def __init__(self, color, wheels, velocity):
        super().__init__(color, wheels)
        self.velocity = velocity

    def __str__(self):
        return super().__str__() + " and Velocity is:" + str(self.velocity)

class Bycicle(Vehicle):
    def __init__(self, color, wheels, types):
        super().__init__(color, wheels)
        self.types = types

    def __str__(self):
        return super().__str__() + " and Type(Urbana/Montaña/Etc):" + str(self.types)


car = Car("Black", 4, 400)
print(car)

bycicle = Bycicle("White", 2, "Ubana")
print(bycicle)