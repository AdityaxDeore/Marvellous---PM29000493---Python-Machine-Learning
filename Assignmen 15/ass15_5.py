# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

def MaxList(ListData):
    return reduce(lambda No1, No2: No1 if No1 > No2 else No2, ListData)

MaxListLambda = lambda ListData: reduce(lambda No1, No2: No1 if No1 > No2 else No2, ListData)

def main():
    Size = int(input("Enter number of elements: "))
    Data = []
    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    Ret1 = MaxList(Data)
    Ret2 = MaxListLambda(Data)
    print("Maximum element using def function is :", Ret1)
    print("Maximum element using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
