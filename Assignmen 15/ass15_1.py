# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

def SquareList(ListData):
    return list(map(lambda No: No ** 2, ListData))

SquareListLambda = lambda ListData: list(map(lambda No: No ** 2, ListData))

def main():
    Size = int(input("Enter number of elements: "))
    Data = []
    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    Ret1 = SquareList(Data)
    Ret2 = SquareListLambda(Data)
    print("List of squares using def function is :", Ret1)
    print("List of squares using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
