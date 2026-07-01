def OddNumbers(Value):
    for i in range(1, Value + 1, 2):
        print(i, end=" ")


def main():
    x = int(input("Enter number : "))
    OddNumbers(x)


if __name__ == "__main__":
    main()
