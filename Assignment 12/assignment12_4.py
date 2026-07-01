def PrintNumbers(Value):
    for i in range(1, Value + 1):
        print(i, end=" ")


def main():
    x = int(input("Enter number : "))
    PrintNumbers(x)


if __name__ == "__main__":
    main()
