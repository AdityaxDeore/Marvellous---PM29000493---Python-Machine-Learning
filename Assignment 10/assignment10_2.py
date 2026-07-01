def SumOfN(Value):
    total = 0
    for i in range(1, Value + 1):
        total = total + i
    print(total)


def main():
    x = int(input("Enter number : "))
    SumOfN(x)


if __name__ == "__main__":
    main()
