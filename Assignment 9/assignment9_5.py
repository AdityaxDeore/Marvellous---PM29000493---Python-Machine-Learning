def CheckDivisible(Value):
    if Value % 3 == 0 and Value % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")


def main():
    x = int(input("Enter number : "))
    CheckDivisible(x)


if __name__ == "__main__":
    main()
