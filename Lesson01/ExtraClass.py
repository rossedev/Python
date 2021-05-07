class Person:
    def __init__(this, names, age, *tupla, **diccionario):
        this.name = names
        this.age = age
        this.val = tupla
        this.dic = diccionario

    def desplegar(self):
        print(self.name, self.age)
        print(self.val)
        print(self.dic)


p1 = Person("Rose",30)
print(p1.name, p1.age)
p1.desplegar()


p2 = Person("Roses", 10, 2, 4, 5)
p2.desplegar()


p3 = Person("Tom", 15, 2, 4, a="apple", b="banana", o="orange")
p3.desplegar()