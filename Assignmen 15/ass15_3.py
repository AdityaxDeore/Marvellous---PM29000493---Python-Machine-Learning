# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

def FilterOdd(ListData):
    return list(filter(lambda No: No % 2 != 0, ListData))

FilterOddLambda = lambda ListData: list(filter(lambda No: No % 2 != 0, ListData))

def main():
    Size = int(input("Enter number of elements: "))
    Data = []
    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    Ret1 = FilterOdd(Data)
    Ret2 = FilterOddLambda(Data)
    print("Odd numbers list using def function is :", Ret1)
    print("Odd numbers list using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
