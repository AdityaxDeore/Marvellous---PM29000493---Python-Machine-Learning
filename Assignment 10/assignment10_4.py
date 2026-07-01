def EvenNumbers(Value):
    for i in range(2, Value + 1, 2):
        print(i, end=" ")


def main():
    x = int(input("Enter number : "))
    EvenNumbers(x)


if __name__ == "__main__":
    main()
