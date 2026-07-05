# Write a lambda function which accepts two numbers and returns maximum number.

def Max(No1, No2):
    return No1 if No1 > No2 else No2

MaxLambda = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    
    Ret1 = Max(Value1, Value2)
    Ret2 = MaxLambda(Value1, Value2)
    
    print("Maximum using def function is :", Ret1)
    print("Maximum using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
