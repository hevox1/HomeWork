class Calculator:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def __add__(self, other):
        return Calculator(self.num1 + self.num2)

c=Calculator(1, 2)