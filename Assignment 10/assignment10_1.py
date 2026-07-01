def Table(Value):
    for i in range(1, 11):
        print(Value * i, end=" ")


def main():
    x = int(input("Enter number : "))
    Table(x)


if __name__ == "__main__":
    main()
