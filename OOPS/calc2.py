class Calculator:

    def __init__(self,*args):
        self.numbers = args

    def add(self):
        return sum(self.numbers)
    
    def sub(self):
        result = 0

        for num in self.numbers:
            result = num - result

            return result
        
cal_insatnce1 = Calculator(10,239,36,25,324)

print(cal_insatnce1.add())
print(cal_insatnce1.sub())