# Design a Python application that creates two threads. Thread 1 should compute the sum of elements from a list. Thread 2 should compute the product of elements from the same list. Return the results to the main thread and display them.

import threading

class SumThread(threading.Thread):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst
        self.result = 0
        
    def run(self):
        self.result = sum(self.lst)

class ProductThread(threading.Thread):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst
        self.result = 1
        
    def run(self):
        if len(self.lst) == 0:
            self.result = 0
            return
        prod = 1
        for x in self.lst:
            prod *= x
        self.result = prod

def main():
    n = int(input("Enter number of elements: "))
    lst = []
    print("Enter elements:")
    for _ in range(n):
        lst.append(int(input()))
        
    t1 = SumThread(lst)
    t2 = ProductThread(lst)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Sum computed by Thread 1:", t1.result)
    print("Product computed by Thread 2:", t2.result)

if __name__ == "__main__":
    main()
