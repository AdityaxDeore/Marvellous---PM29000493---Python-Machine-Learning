# Design a Python application that creates two threads named EvenList and OddList. Both threads should accept a list of integers as input. The EvenList thread should extract all even elements from the list and calculate and display their sum. The OddList thread should extract all odd elements from the list and calculate and display their sum. Threads should run concurrently.

import threading

def EvenList(lst):
    total = sum(x for x in lst if x % 2 == 0)
    print(f"EvenList Thread: Sum of even elements is {total}")

def OddList(lst):
    total = sum(x for x in lst if x % 2 != 0)
    print(f"OddList Thread: Sum of odd elements is {total}")

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter elements:")
    for _ in range(n):
        lst.append(int(input()))
        
    t1 = threading.Thread(target=EvenList, args=(lst,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(lst,), name="OddList")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
