class InputDevice:
    def __init__(self, typeInput, brand):
        self._typeInput = typeInput
        self._brand = brand

    def __str__(self):
        return "type input is: " + self._typeInput + " and the brand is: " + self._brand

    def getTypeInput(self):
        return self._typeInput

    def setTypeInput(self, typeInput):
        self._typeInput = typeInput

    def getBrand(self):
        return self._brand

    def setBrand(self, brand):
        self._brand = brand

