# Write a program which accepts number from user and returns addition of digits in that number.

def SumDigits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

def main():
    val = int(input("Enter a number: "))
    ans = SumDigits(val)
    print("Sum of digits:", ans)

if __name__ == "__main__":
    main()
