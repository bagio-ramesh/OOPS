class Calculator:

    def __init__(self,num1,num2):

        self.num1 = num1

        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2
        
    def mul(self):
        return self.num1 * self.num2

cal_instance1 = Calculator(100,5)
print(cal_instance1.add())
print(cal_instance1.sub())
print(cal_instance1.mul())