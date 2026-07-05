# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

def AdditionList(ListData):
    return reduce(lambda No1, No2: No1 + No2, ListData)

AdditionListLambda = lambda ListData: reduce(lambda No1, No2: No1 + No2, ListData)

def main():
    Size = int(input("Enter number of elements: "))
    Data = []
    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    Ret1 = AdditionList(Data)
    Ret2 = AdditionListLambda(Data)
    print("Addition using def function is :", Ret1)
    print("Addition using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
