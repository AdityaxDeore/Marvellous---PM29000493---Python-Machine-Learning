class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def CheckPrime(self):
        if self.Value < 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def checkPerfect(self):
        if self.Value < 1:
            return False
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum == self.Value

    def Factors(self):
        factors = []
        for i in range(1, self.Value):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def sumFactors(self):
        sum = 0
        for factor in self.Factors():
            sum += factor
        return sum

#create objects
obj = Numbers(10)
print(obj.CheckPrime())
print(obj.checkPerfect())
print(obj.Factors())
print(obj.sumFactors())
