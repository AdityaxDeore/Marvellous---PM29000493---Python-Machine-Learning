# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

def FilterStrings(StrList):
    return list(filter(lambda Str: len(Str) > 5, StrList))

FilterStringsLambda = lambda StrList: list(filter(lambda Str: len(Str) > 5, StrList))

def main():
    Size = int(input("Enter number of strings: "))
    Data = []
    print("Enter the strings:")
    for i in range(Size):
        Str = input()
        Data.append(Str)
    
    Ret1 = FilterStrings(Data)
    Ret2 = FilterStringsLambda(Data)
    print("Strings with length > 5 using def function is :", Ret1)
    print("Strings with length > 5 using lambda function is :", Ret2)

if __name__ == "__main__":
    main()
