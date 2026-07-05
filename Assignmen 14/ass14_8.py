# Write a lambda function which accepts two numbers and returns addition.

def Add(No1, No2):
    return No1 + No2

AddLambda = lambda No1, No2: No1 + No2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    
    Ret1 = Add(Value1, Value2)
    Ret2 = AddLambda(Value1, Value2)
    
    print("Addition using def function is :", Ret1)
    print("Addition using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
