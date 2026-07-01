def CheckPerfect(Value):
    total = 0
    for i in range(1, Value):
        if Value % i == 0:
            total = total + i
    if total == Value:
        print("Perfect Number")
    else:
        print("Not Perfect Number")


def main():
    x = int(input("Enter number : "))
    CheckPerfect(x)


if __name__ == "__main__":
    main()
