# Write a program which accepts one number and displays the given increasing triangular number pattern.

def DisplayIncreasingNumberPattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{j} ", end="")
        print()

def main():
    val = int(input("Enter a number: "))
    DisplayIncreasingNumberPattern(val)

if __name__ == "__main__":
    main()
