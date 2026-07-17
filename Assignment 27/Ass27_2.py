class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Name: {self.Name}, Amount: {self.Amount}")

    def Deposit(self, Amount):
        self.Amount += Amount

    def Withdraw(self, Amount):
        if self.Amount >= Amount:
            self.Amount -= Amount
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        print(f"Interest: {self.Amount * (self.ROI / 100)}")



#object creation
obj1 = BankAccount("Aditya", 1000)
obj1.Display()
obj1.Deposit(500)
obj1.Display()
obj1.Withdraw(200)
obj1.Display()
print(obj1.CalculateInterest())
