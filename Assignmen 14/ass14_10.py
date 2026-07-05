# Write a lambda function which accepts three numbers and returns largest number.

def Largest(No1, No2, No3):
    return No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)

LargestLambda = lambda No1, No2, No3: No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    Value3 = int(input("Enter third number: "))
    
    Ret1 = Largest(Value1, Value2, Value3)
    Ret2 = LargestLambda(Value1, Value2, Value3)
    
    print("Largest number using def function is :", Ret1)
    print("Largest number using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
