class Calculator:

    def sum(self, num1: int, num2: int):
        return num1 + num2

    def multiplication(self, num1: int, num2: int):
        return num1 * num2

    def subtraction(self, num1: int, num2: int):
        return num1 - num2

    def division(self, num1: int, num2: int):
        if num2 > 0:
            return num1 / num2
