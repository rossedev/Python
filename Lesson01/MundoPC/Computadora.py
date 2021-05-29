class Computer:
    countComputer = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.countComputer += 1
        self.__idComputer = Computer.countComputer
        self.__name = name
        self.__monitor = monitor
        self.__keyboard = keyboard
        self.__mouse = mouse

    def __str__(self):
        return (
            f"""
            { self.__name } : { self.__idComputer }
            Monitor : { self.__monitor }
            Keyboard: { self.__keyboard }
            Mouse: { self.__mouse }
            """
        )

    def getIdComputer(self):
        return self.__idComputer

    def setIdComputer(self, idComputer):
        self.__idComputer = idComputer

    def getName(self):
        return self.name

    def setName(self, name):
        self.__name = name

    def getMonitor(self):
        return self.__monitor

    def setKeyboard(self, keyboard):
        self.__keyboard = keyboard

    def getKeyboard(self):
        return self.keyboard

    def setMonitor(self, monitor):
        self.__monitor = monitor

    def getMouse(self):
        return self.mouse

    def setMouse(self, mouse):
        self.__mouse = mouse


