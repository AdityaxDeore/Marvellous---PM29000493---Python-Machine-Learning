# Write a lambda function which accepts one number and returns square of that number.

def Square(No):
    return No ** 2

SquareLambda = lambda No: No ** 2

def main():
    Value = int(input("Enter a number: "))
    
    Ret1 = Square(Value)
    Ret2 = SquareLambda(Value)
    
    print("Square using def function is :", Ret1)
    print("Square using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
