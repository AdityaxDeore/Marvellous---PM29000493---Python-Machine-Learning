# Write a program which accepts number from user and returns number of digits in that number.

def CountDigits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

def main():
    val = int(input("Enter a number: "))
    ans = CountDigits(val)
    print("Number of digits:", ans)

if __name__ == "__main__":
    main()
