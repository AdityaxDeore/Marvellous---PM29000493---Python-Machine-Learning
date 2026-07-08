# Write a program which accepts number from user and checks whether that number is positive, negative or zero.

def ChkNumber(number):
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

def main():
    val = int(input("Enter a number: "))
    ChkNumber(val)

if __name__ == "__main__":
    main()
