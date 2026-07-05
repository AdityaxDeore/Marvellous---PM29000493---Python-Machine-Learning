# 10. Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

def CountEven(ListData):
    return len(list(filter(lambda No: No % 2 == 0, ListData)))

CountEvenLambda = lambda ListData: len(list(filter(lambda No: No % 2 == 0, ListData)))

def main():
    Size = int(input("Enter number of elements: "))
    Data = []
    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    Ret1 = CountEven(Data)
    Ret2 = CountEvenLambda(Data)
    print("Count of even numbers using def function is :", Ret1)
    print("Count of even numbers using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
