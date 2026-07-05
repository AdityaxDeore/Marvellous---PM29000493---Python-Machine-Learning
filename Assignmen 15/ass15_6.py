# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

def MinList(ListData):
    return reduce(lambda No1, No2: No1 if No1 < No2 else No2, ListData)

MinListLambda = lambda ListData: reduce(lambda No1, No2: No1 if No1 < No2 else No2, ListData)

def main():
    Size = int(input("Enter number of elements: "))
    Data = []
    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    Ret1 = MinList(Data)
    Ret2 = MinListLambda(Data)
    print("Minimum element using def function is :", Ret1)
    print("Minimum element using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
