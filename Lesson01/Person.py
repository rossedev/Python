class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


Person.name = "Rose"
Person.age = 19

print(Person.name, Person.age)

# create object
person = Person("Dani", 20)
print(person.name, person.age)
print(id(person))

person2 = Person("Loviu", 60)
print(person2.name, person2.age)
print(id(person2))