# Write a lambda function which accepts one number and returns True if number is even otherwise False.

def IsEven(No):
    return No % 2 == 0

IsEvenLambda = lambda No: No % 2 == 0

def main():
    Value = int(input("Enter a number: "))
    
    Ret1 = IsEven(Value)
    Ret2 = IsEvenLambda(Value)
    
    print("Is Even using def function is :", Ret1)
    print("Is Even using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
