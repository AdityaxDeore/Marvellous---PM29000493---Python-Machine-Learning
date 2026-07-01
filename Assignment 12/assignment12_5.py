def PrintReverse(Value):
    for i in range(Value, 0, -1):
        print(i, end=" ")


def main():
    x = int(input("Enter number : "))
    PrintReverse(x)


if __name__ == "__main__":
    main()
