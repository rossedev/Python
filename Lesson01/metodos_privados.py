class Person:
    def __init__(self, name, fist_name, second_name):
        self.name = name
        self._fist_lastname = fist_name
        self.__second_lastname = second_name

    def publicMethod(self):
        self.__privateMethod()

    def __privateMethod(self):
        print(self.name)
        print(self._fist_lastname)
        print(self.__second_lastname)

    def get_second_lastname(self):
        return self.__second_lastname

    def set_second_lastname(self, second_lastname):
        self.__second_lastname = second_lastname


p1 = Person("Dan", "Kop", "Kap")

p1.publicMethod()

print(p1.name)
print(p1._fist_lastname)
print(p1.get_second_lastname())