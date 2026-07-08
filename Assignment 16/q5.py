# Write a program which displays 10 to 1 on screen.

def Display():
    for i in range(10, 0, -1):
        print(i, end=" ")
    print()

def main():
    Display()

if __name__ == "__main__":
    main()
