# Design a Python application that creates two separate threads named Even and Odd. The Even thread should display the first 10 even numbers. The Odd thread should display the first 10 odd numbers. Both threads should execute independently using the threading module. Ensure proper thread creation and execution.

import threading

def Even():
    print("Even Thread is displaying first 10 even numbers:")
    num = 2
    for _ in range(10):
        print(num, end=" ")
        num += 2
    print()

def Odd():
    print("Odd Thread is displaying first 10 odd numbers:")
    num = 1
    for _ in range(10):
        print(num, end=" ")
        num += 2
    print()

def main():
    t1 = threading.Thread(target=Even, name="Even")
    t2 = threading.Thread(target=Odd, name="Odd")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
