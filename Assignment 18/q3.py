# Write a program which accepts N numbers from user and stores them into List. Return Minimum number from that List.

def MinElement(lst):
    if len(lst) == 0:
        return None
    minimum = lst[0]
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter the elements:")
    for _ in range(n):
        lst.append(int(input()))
    
    ans = MinElement(lst)
    print("Minimum element is:", ans)

if __name__ == "__main__":
    main()
