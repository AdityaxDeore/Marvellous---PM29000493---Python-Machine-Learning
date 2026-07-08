# Create one module named Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accept two parameters as numbers and perform the operation.

def Add(no1, no2):
    return no1 + no2

def Sub(no1, no2):
    return no1 - no2

def Mult(no1, no2):
    return no1 * no2

def Div(no1, no2):
    if no2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return no1 / no2
