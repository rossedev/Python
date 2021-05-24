class Monitor:
    countMonitor = 0

    def __init__(self, brand, size):
        Monitor.countMonitor += 1
        self.__idMonitor = Monitor.countMonitor
        self.__brand = brand
        self.__size = size

    def __str__(self):
        return "id Monitor " + str(self.__idMonitor) + " Brand " + self.__brand + " Size " + str(self.__size)

    def getIdMonitor(self):
        return self.__idMonitor

    def setIdMonitor(self, idMonitor):
        self.__idMonitor = idMonitor

    def getBrand(self):
        return self.__brand

    def setBrand(self, brand):
        self.__brand = brand

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

