# Write a lambda function which accepts two numbers and returns multiplication.

def Mult(No1, No2):
    return No1 * No2

MultLambda = lambda No1, No2: No1 * No2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    
    Ret1 = Mult(Value1, Value2)
    Ret2 = MultLambda(Value1, Value2)
    
    print("Multiplication using def function is :", Ret1)
    print("Multiplication using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
