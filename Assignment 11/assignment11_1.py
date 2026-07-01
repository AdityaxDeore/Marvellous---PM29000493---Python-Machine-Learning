def CheckPrime(Value):
    if Value < 2:
        print("Not Prime Number")
        return
    for i in range(2, Value):
        if Value % i == 0:
            print("Not Prime Number")
            return
    print("Prime Number")


def main():
    x = int(input("Enter number : "))
    CheckPrime(x)


if __name__ == "__main__":
    main()
