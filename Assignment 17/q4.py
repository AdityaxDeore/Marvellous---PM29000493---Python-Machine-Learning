# Write a program which accepts one number from user and returns addition of its factors.

def SumFactors(n):
    total = 0
    # Factors of N are numbers that divide N exactly
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

def main():
    val = int(input("Enter a number: "))
    ans = SumFactors(val)
    print("Sum of factors is:", ans)

if __name__ == "__main__":
    main()
