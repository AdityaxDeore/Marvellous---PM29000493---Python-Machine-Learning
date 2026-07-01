def Grade(Marks):
    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60:
        print("First Class")
    elif Marks >= 50:
        print("Second Class")
    else:
        print("Fail")


def main():
    x = int(input("Enter marks : "))
    Grade(x)


if __name__ == "__main__":
    main()
