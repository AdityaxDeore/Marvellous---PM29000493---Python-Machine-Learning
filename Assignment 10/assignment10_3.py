def Factorial(Value):
    fact = 1
    for i in range(1, Value + 1):
        fact = fact * i
    print(fact)


def main():
    x = int(input("Enter number : "))
    Factorial(x)


if __name__ == "__main__":
    main()
