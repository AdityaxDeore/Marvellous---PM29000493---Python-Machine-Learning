# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

def FilterEven(ListData):
    return list(filter(lambda No: No % 2 == 0, ListData))

FilterEvenLambda = lambda ListData: list(filter(lambda No: No % 2 == 0, ListData))

def main():
    Size = int(input("Enter number of elements: "))
    Data = []
    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    Ret1 = FilterEven(Data)
    Ret2 = FilterEvenLambda(Data)
    print("Even numbers list using def function is :", Ret1)
    print("Even numbers list using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
