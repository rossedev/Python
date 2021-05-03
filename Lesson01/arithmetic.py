class Arithmetic:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def add(self):
        """ Se realiza la operacion con los atributos  de la clase"""
        return self.operand1 + self.operand2


arithmetic = Arithmetic(2, 6)
print("Add result", arithmetic.add())