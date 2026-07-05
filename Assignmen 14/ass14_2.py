# Write a lambda function which accepts one number and returns cube of that number.

def Cube(No):
    return No ** 3

CubeLambda = lambda No: No ** 3

def main():
    Value = int(input("Enter a number: "))
    
    Ret1 = Cube(Value)
    Ret2 = CubeLambda(Value)
    
    print("Cube using def function is :", Ret1)
    print("Cube using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
