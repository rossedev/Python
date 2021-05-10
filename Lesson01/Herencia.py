class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name:" + self.name + ", age:" + str(self.age)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return super().__str__() + ", Salary:" + str(self.salary)


person = Person("Rose", 10)
print(person)

employee = Employee("Dan",12,30.00)
print(employee)

employee.name = "YO"
employee.salary = 800.00

print(employee)