def ChkGreater(Value1,Value2):
    if Value1 > Value2:
        print(Value1, "is greater")
    else:
        print(Value2, "is greater")


def main():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    ChkGreater(x,y)


if __name__ == "__main__":
    main()
