# Write a program which accepts one number from user and checks whether that number is prime or not.

def ChkPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    val = int(input("Enter a number: "))
    if ChkPrime(val):
        print("It is a Prime number")
    else:
        print("It is not a Prime number")

if __name__ == "__main__":
    main()
