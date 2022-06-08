from operations import interface

class Multiplication(interface.Operation):
    def __init__(self, args):
        self.__args__ = args

    def calculate(self) -> int:
        result = 1
        for elem in self.__args__:
            result *= int(elem)
        return result