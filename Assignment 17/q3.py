# Write a program which accepts one number from user and returns its factorial.

def Factorial(n):
    if n < 0:
        return None
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def main():
    val = int(input("Enter a number: "))
    ans = Factorial(val)
    print("Factorial is:", ans)

if __name__ == "__main__":
    main()
