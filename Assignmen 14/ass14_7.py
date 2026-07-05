# Write a lambda function which accepts one number and returns True if divisible by 5.

def DivisibleBy5(No):
    return No % 5 == 0

DivisibleBy5Lambda = lambda No: No % 5 == 0

def main():
    Value = int(input("Enter a number: "))
    
    Ret1 = DivisibleBy5(Value)
    Ret2 = DivisibleBy5Lambda(Value)
    
    print("Is divisible by 5 using def function is :", Ret1)
    print("Is divisible by 5 using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
