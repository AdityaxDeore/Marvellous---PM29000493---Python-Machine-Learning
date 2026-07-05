# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

def FilterDivisible(ListData):
    return list(filter(lambda No: No % 3 == 0 and No % 5 == 0, ListData))

FilterDivisibleLambda = lambda ListData: list(filter(lambda No: No % 3 == 0 and No % 5 == 0, ListData))

def main():
    Size = int(input("Enter number of elements: "))
    Data = []
    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    Ret1 = FilterDivisible(Data)
    Ret2 = FilterDivisibleLambda(Data)
    print("Numbers divisible by 3 and 5 using def function is :", Ret1)
    print("Numbers divisible by 3 and 5 using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
