def CheckPalindrome(Value):
    temp = Value
    rev = 0
    while Value != 0:
        rev = (rev * 10) + (Value % 10)
        Value = Value // 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


def main():
    x = int(input("Enter number : "))
    CheckPalindrome(x)


if __name__ == "__main__":
    main()
