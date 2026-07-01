def Factors(Value):
    for i in range(1, Value + 1):
        if Value % i == 0:
            print(i, end=" ")


def main():
    x = int(input("Enter number : "))
    Factors(x)


if __name__ == "__main__":
    main()
