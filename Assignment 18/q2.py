# Write a program which accepts N numbers from user and stores them into List. Return Maximum number from that List.

def MaxElement(lst):
    if len(lst) == 0:
        return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter the elements:")
    for _ in range(n):
        lst.append(int(input()))
    
    ans = MaxElement(lst)
    print("Maximum element is:", ans)

if __name__ == "__main__":
    main()
