# Write a program which accepts N numbers from user and stores them into List. Accept one another number from user and return frequency of that number from List.

def FrequencyElement(lst, value):
    count = 0
    for num in lst:
        if num == value:
            count += 1
    return count

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter the elements:")
    for _ in range(n):
        lst.append(int(input()))
    
    search_value = int(input("Enter number to check frequency: "))
    ans = FrequencyElement(lst, search_value)
    print("Frequency of the number is:", ans)

if __name__ == "__main__":
    main()
