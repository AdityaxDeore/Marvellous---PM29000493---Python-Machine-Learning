# Write a program which accepts number from user and prints that number of * on screen.

def DisplayPattern(number):
    print("*" * number)

def main():
    val = int(input("Enter a number: "))
    DisplayPattern(val)

if __name__ == "__main__":
    main()
