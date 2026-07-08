# Write a program which contains one function named ChkNum() which accepts one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.

def ChkNum(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def main():
    val = int(input("Enter a number: "))
    ChkNum(val)

if __name__ == "__main__":
    main()
