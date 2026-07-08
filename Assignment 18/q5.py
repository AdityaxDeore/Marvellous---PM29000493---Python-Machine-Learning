# Write a program which accepts N numbers from user and stores them into List. Return addition of all prime numbers from that List. Main Python file accepts N numbers from user and passes each number to ChkPrime() function which is part of your user-defined module named MarvellousNum. Name of the function from main Python file should be ListPrime().

import MarvellousNum

def ListPrime(lst):
    total = 0
    for num in lst:
        if MarvellousNum.ChkPrime(num):
            total += num
    return total

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter the elements:")
    for _ in range(n):
        lst.append(int(input()))
    
    ans = ListPrime(lst)
    print("Addition of prime numbers is:", ans)

if __name__ == "__main__":
    main()
