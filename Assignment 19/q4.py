# Write a program which contains filter(), map() and reduce() in it. Python application contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

from functools import reduce

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter the elements:")
    for _ in range(n):
        lst.append(int(input()))
    
    print("Input List:", lst)
    
    # Filter: Even numbers
    filtered_list = list(filter(lambda x: x % 2 == 0, lst))
    print("Filtered List (Even):", filtered_list)
    
    # Map: Squares
    mapped_list = list(map(lambda x: x ** 2, filtered_list))
    print("Mapped List (Squares):", mapped_list)
    
    # Reduce: Addition of all numbers
    if len(mapped_list) > 0:
        addition = reduce(lambda x, y: x + y, mapped_list)
        print("Addition of elements is:", addition)
    else:
        print("Sum of elements is: 0")

if __name__ == "__main__":
    main()
