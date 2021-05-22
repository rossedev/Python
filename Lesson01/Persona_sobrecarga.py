class Person:
    def __init__(self, name):
        self.__name = name

    def __add__(self, other):
        return self.__name + " " + other.__name

    def __sub__(self, other):
        return "Hi, honey :3"


p1 = Person("Rose")
p2 = Person("Dan")

print(p1 + p2)

print(p1 - p2)