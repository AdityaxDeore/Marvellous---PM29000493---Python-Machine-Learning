# Write a program which contains one lambda function which accepts two parameters and returns its multiplication.

Multiply = lambda x, y: x * y

def main():
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    print("Multiplication is:", Multiply(val1, val2))

if __name__ == "__main__":
    main()
