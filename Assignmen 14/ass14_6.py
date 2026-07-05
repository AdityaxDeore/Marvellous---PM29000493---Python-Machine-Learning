# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

def IsOdd(No):
    return No % 2 != 0

IsOddLambda = lambda No: No % 2 != 0

def main():
    Value = int(input("Enter a number: "))
    
    Ret1 = IsOdd(Value)
    Ret2 = IsOddLambda(Value)
    
    print("Is Odd using def function is :", Ret1)
    print("Is Odd using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
