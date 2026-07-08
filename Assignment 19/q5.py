# Write a program which contains filter(), map() and reduce() in it. Python application contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. You can also use normal functions instead of lambda functions.

from functools import reduce

def ChkPrime(No):
    if No <= 1:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter the elements:")
    for _ in range(n):
        lst.append(int(input()))
    
    print("Input List:", lst)
    
    # Filter: Prime numbers
    filtered_list = list(filter(ChkPrime, lst))
    print("Filtered List (Primes):", filtered_list)
    
    # Map: Multiply by 2
    mapped_list = list(map(lambda x: x * 2, filtered_list))
    print("Mapped List (Multiplied by 2):", mapped_list)
    
    # Reduce: Maximum
    if len(mapped_list) > 0:
        maximum = reduce(lambda x, y: x if x > y else y, mapped_list)
        print("Maximum number is:", maximum)
    else:
        print("Maximum cannot be computed for an empty list.")

if __name__ == "__main__":
    main()
