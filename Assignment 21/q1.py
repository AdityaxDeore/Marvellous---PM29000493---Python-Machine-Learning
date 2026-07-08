# Design a Python application that creates two threads named Prime and NonPrime. Both threads should accept a list of integers. The Prime thread should display all prime numbers from the list. The NonPrime thread should display all non-prime numbers from the list.

import threading

def ChkPrime(No):
    if No <= 1:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def Prime(lst):
    primes = [x for x in lst if ChkPrime(x)]
    print("Prime Thread: Prime numbers in the list are:", primes)

def NonPrime(lst):
    non_primes = [x for x in lst if not ChkPrime(x)]
    print("NonPrime Thread: Non-prime numbers in the list are:", non_primes)

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter elements:")
    for _ in range(n):
        lst.append(int(input()))
        
    t1 = threading.Thread(target=Prime, args=(lst,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(lst,), name="NonPrime")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
