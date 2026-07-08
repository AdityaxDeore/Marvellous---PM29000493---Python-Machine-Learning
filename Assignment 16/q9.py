# Write a program which displays first 10 even numbers on screen.

def DisplayEven():
    count = 0
    num = 2
    while count < 10:
        print(num, end=" ")
        num += 2
        count += 1
    print()

def main():
    DisplayEven()

if __name__ == "__main__":
    main()
