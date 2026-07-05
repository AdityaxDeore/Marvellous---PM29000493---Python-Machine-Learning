# Write a lambda function which accepts two numbers and returns minimum number.

def Min(No1, No2):
    return No1 if No1 < No2 else No2

MinLambda = lambda No1, No2: No1 if No1 < No2 else No2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    
    Ret1 = Min(Value1, Value2)
    Ret2 = MinLambda(Value1, Value2)
    
    print("Minimum using def function is :", Ret1)
    print("Minimum using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
