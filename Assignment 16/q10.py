# Write a program which accepts name from user and displays length of its name.

def DisplayLength(name):
    print("Length of the name is:", len(name))

def main():
    name = input("Enter your name: ")
    DisplayLength(name)

if __name__ == "__main__":
    main()
