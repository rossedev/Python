class MyClass:
    var_class = "Class of var"

    def __init__(self, var_instance):
        self.var_instance = var_instance


print(MyClass.var_class)
obj1 = MyClass("Hi!")
MyClass.var_instance = "Distict"
print(obj1.var_instance)
print(MyClass.var_instance)

# Podemos acceder a las variables de clases desde los objetos
print(obj1.var_class)
# Podemos acceder a las variables con el nombre de la clase
print(MyClass.var_class)

obj1.var_class =" Modify var class"
print(obj1.var_class)
print(MyClass.var_class)

obj2 = MyClass("New var")
print(obj2.var_class)

obj3 = MyClass("New var three")
MyClass.var_class = "New var in class"
print(obj1.var_class)
print(obj2.var_class)
print(obj3.var_class)