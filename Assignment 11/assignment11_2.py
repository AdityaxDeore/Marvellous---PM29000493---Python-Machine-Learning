def CountDigits(Value):
    count = 0
    while Value != 0:
        count = count + 1
        Value = Value // 10
    print(count)


def main():
    x = int(input("Enter number : "))
    CountDigits(x)


if __name__ == "__main__":
    main()
