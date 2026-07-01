def SumDigits(Value):
    total = 0
    while Value != 0:
        total = total + (Value % 10)
        Value = Value // 10
    print(total)


def main():
    x = int(input("Enter number : "))
    SumDigits(x)


if __name__ == "__main__":
    main()
