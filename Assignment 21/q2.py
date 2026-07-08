# Design a Python application that creates two threads. Thread 1 should calculate and display the maximum element from a list. Thread 2 should calculate and display the minimum element from the same list. The list should be accepted from the user.

import threading

def FindMax(lst):
    if len(lst) == 0:
        print("Max Thread: List is empty")
        return
    print("Max Thread: Maximum element is:", max(lst))

def FindMin(lst):
    if len(lst) == 0:
        print("Min Thread: List is empty")
        return
    print("Min Thread: Minimum element is:", min(lst))

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter elements:")
    for _ in range(n):
        lst.append(int(input()))
        
    t1 = threading.Thread(target=FindMax, args=(lst,), name="MaxThread")
    t2 = threading.Thread(target=FindMin, args=(lst,), name="MinThread")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
