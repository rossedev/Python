class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "Name: " + self.name + " salary: " + str(self.salary)


