# Write a program which accepts one number and displays the given square pattern.

def DisplaySquarePattern(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()

def main():
    val = int(input("Enter a number: "))
    DisplaySquarePattern(val)

if __name__ == "__main__":
    main()
