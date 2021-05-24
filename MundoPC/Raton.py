from DispositivoEntrada import InputDevice
class Mouse(InputDevice):
    countMouses = 0

    def __init__(self, typeInput, brand):
        Mouse.countMouses += 1
        self.__idMouse = Mouse.countMouses
        self._typeInput = typeInput
        self._brand = brand

    def __str__(self):
        return "id Mouse " + str(self.__idMouse) + " typeInput " + self._typeInput + " brand " + self._brand
