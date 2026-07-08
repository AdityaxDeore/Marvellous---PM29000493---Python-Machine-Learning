# Write a program which contains one lambda function which accepts one parameter and returns power of two.

PowerOfTwo = lambda x: 2 ** x

def main():
    val = int(input("Enter number: "))
    print(f"2 power {val} is:", PowerOfTwo(val))

if __name__ == "__main__":
    main()
