from empleado import Employee
from gerente import Manager


def print_details(object):
    print(type(object))
    print(object, end="\n\n")
    if isinstance(object, Manager):
        print(object.departament)


employee = Employee("Rose", 2.000)
print_details(employee)

employee = Manager("Dan", 3.000,"Technology")
print_details(employee)