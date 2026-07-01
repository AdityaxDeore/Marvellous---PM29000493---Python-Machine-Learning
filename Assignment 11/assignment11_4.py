def ReverseNumber(Value):
    rev = 0
    while Value != 0:
        rev = (rev * 10) + (Value % 10)
        Value = Value // 10
    print(rev)


def main():
    x = int(input("Enter number : "))
    ReverseNumber(x)


if __name__ == "__main__":
    main()
