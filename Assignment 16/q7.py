# Write a program which contains one function that accepts one number from user and returns True if number is divisible by 5 otherwise returns False.

def ChkDivisibleBy5(number):
    return number % 5 == 0

def main():
    val = int(input("Enter a number: "))
    ret = ChkDivisibleBy5(val)
    print(ret)

if __name__ == "__main__":
    main()
