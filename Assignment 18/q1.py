# Write a program which accepts N numbers from user and stores them into List. Return addition of all elements from that List.

def SumElements(lst):
    total = 0
    for num in lst:
        total += num
    return total

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter the elements:")
    for _ in range(n):
        lst.append(int(input()))
    
    ans = SumElements(lst)
    print("Sum of elements is:", ans)

if __name__ == "__main__":
    main()
