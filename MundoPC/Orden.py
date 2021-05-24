class Order:
    countOrders = 0

    def __init__(self, computers):
        Order.countOrders += 1
        self.__idOrder = Order.countOrders
        self.__computers = computers

    def addComputer(self, computer):
        self.__computers.append(computer)

    def __str__(self):
        computerStr = ""

        for computers in self.__computers:
            computerStr += computers.__str__()

        return "id Order: " + str(self.__idOrder) + " \n Computer: " + computerStr

