user_meaning = int(input('Введите номер операции которые вы бы хотели произвести:\n1 - (+)\n2 - (-)\n3 - (*)\n4 - (/)\n'))
user_num1 = int(input('Отлично, теперь введите первое число: '))
user_num2 = int(input('И второе число: '))

class Calculator:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        return print(self.num1 + self.num2)
    def sub(self):
        return print(self.num1 - self.num2)
    def multi(self):
        return print(self.num1 * self.num2)
    def div(self):
        return print(self.num1 // self.num2)

c=Calculator(user_num1, user_num2)
if user_meaning == 1:
    c.sum()
elif user_meaning == 2:
    c.sub()
elif user_meaning == 3:
    c.multi()
elif user_meaning == 4:
    c.div()