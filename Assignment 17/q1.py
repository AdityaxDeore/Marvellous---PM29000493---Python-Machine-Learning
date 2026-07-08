# Create one module named Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accept two parameters as numbers and perform the operation. Write one Python program which calls all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    val1 = float(input("Enter first number: "))
    val2 = float(input("Enter second number: "))
    
    print("Addition is:", Arithmetic.Add(val1, val2))
    print("Subtraction is:", Arithmetic.Sub(val1, val2))
    print("Multiplication is:", Arithmetic.Mult(val1, val2))
    try:
        print("Division is:", Arithmetic.Div(val1, val2))
    except ZeroDivisionError as e:
        print("Division is:", e)

if __name__ == "__main__":
    main()
