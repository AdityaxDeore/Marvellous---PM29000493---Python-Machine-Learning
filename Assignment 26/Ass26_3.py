class Arithmetic:
    value1 = 0
    value2 = 0

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def Accept(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1 / self.value2

#create objects
obj = Arithmetic(5,10)

#calling methods on objects
print(obj.Addition())
print(obj.Subtraction())
print(obj.Multiplication())
print(obj.Division())
