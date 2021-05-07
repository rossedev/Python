class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


p1 = Person("Ro",25)
print(p1.get_name())
print(p1.get_age())

p1.set_name("Da")
print(p1.get_name())

p1.set_age(21)
print(p1.get_age())