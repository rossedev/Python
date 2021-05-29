from DispositivoEntrada import InputDevice


class Keyboard(InputDevice):
    countKeyboards = 0

    def __init__(self, typeInput, brand):
        Keyboard.countKeyboards += 1
        self.__idKeyboard = Keyboard.countKeyboards
        self._typeInput = typeInput
        self._brand = brand

    def __str__(self):
        return "id Keyboard " + str(self.__idKeyboard) + " typeInput " + self._typeInput + " brand " + self._brand
