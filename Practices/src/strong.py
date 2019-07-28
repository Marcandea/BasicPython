class Strong:
    def strongNumber(self, num1: int):
        string = str(num1)
        num = 0
        mult = 1
        result = 0
        if num1 < 0:
            return "Negative Number"
        for i in string:
            entero = int(i)
            for n in range(entero):
                num = entero - n
                mult = mult * num

                # print(num,mult)

            result = mult + result
            mult = 1

        if result == num1:
            return "Strong"
        else:
            return "No Strong"
