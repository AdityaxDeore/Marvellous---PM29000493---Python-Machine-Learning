def Arithmetic(Value1,Value2):
    print("Addition :", Value1 + Value2)
    print("Subtraction :", Value1 - Value2)
    print("Multiplication :", Value1 * Value2)
    print("Division :", Value1 / Value2)


def main():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    Arithmetic(x,y)


if __name__ == "__main__":
    main()
