from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    def __init__(self, width, high):
        self.__width = width
        self.__high = high

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_high(self):
        return self.__high

    def set_high(self, high):
        self.__high = high

    def __str__(self):
        return "Width: " + str(self.get_width()) + " High " + str(self.get_high())

    @abstractmethod
    def area(self):
        pass