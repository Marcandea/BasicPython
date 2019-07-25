class Fibonacci:
    def fi(self, num1: int, num2: int, start: int):
        result = str(num1) + str(num2)
        for i in range(start):
            sum = num1 + num2
            result = result + str(sum)
            num1 = num2
            num2 = sum
#comodim
        return result
