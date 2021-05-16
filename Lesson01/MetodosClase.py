class MyClass:

    class_var = "class Variable"

    def __init__(self):
        self.instance_var = "Instance Var"

    @staticmethod
    def static_method():
        print("Estatic Method!")
        print(MyClass.class_var)
        # Desde un metodo estatico no se puede acceder a una variable de instancia

    @classmethod
    def class_method(cls):
        print("Class method" + str(cls))
        print(cls.class_var)
        # Desde un contexto estatico (metodo de clase) no se puede acceder a una variable de instancia

    def instance_method(self):
        self.static_method()
        self.class_method()
        print(self.instance_var)
        print(self.class_var)


MyClass.static_method()
MyClass.class_method()

print("\n diferent******")
obj1 = MyClass()
obj1.instance_method()