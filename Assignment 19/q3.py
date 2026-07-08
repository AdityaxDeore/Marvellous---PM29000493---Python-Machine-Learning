# Write a program which contains filter(), map() and reduce() in it. Python application contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

from functools import reduce

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter the elements:")
    for _ in range(n):
        lst.append(int(input()))
    
    print("Input List:", lst)
    
    # Filter: numbers >= 70 and <= 90
    filtered_list = list(filter(lambda x: 70 <= x <= 90, lst))
    print("Filtered List (>=70 and <=90):", filtered_list)
    
    # Map: increase each by 10
    mapped_list = list(map(lambda x: x + 10, filtered_list))
    print("Mapped List (increased by 10):", mapped_list)
    
    # Reduce: product of all numbers
    if len(mapped_list) > 0:
        product = reduce(lambda x, y: x * y, mapped_list)
        print("Product of elements is:", product)
    else:
        print("Product cannot be computed for an empty list.")

if __name__ == "__main__":
    main()
