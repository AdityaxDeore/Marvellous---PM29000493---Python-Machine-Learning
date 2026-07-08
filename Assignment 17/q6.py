# Write a program which accepts one number and displays the given inverted star pattern.

def DisplayInvertedPattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

def main():
    val = int(input("Enter a number: "))
    DisplayInvertedPattern(val)

if __name__ == "__main__":
    main()
