# Write a program which accepts one number and displays the given repeated-number square pattern.

def DisplayRepeatedNumberPattern(n):
    for i in range(1, n + 1):
        for j in range(n):
            print(f"{i} ", end="")
        print()

def main():
    val = int(input("Enter a number: "))
    DisplayRepeatedNumberPattern(val)

if __name__ == "__main__":
    main()
