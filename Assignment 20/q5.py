# Design a Python application that creates two threads named Thread1 and Thread2. Thread1 should display numbers from 1 to 50. Thread2 should display numbers from 50 to 1 in reverse order. Ensure that Thread2 starts execution only after Thread1 has completed. Use appropriate thread synchronization.

import threading
import time

def Thread1():
    print("Thread1 starting...")
    for i in range(1, 51):
        print(i, end=" ")
    print("\nThread1 completed.")

def Thread2():
    print("Thread2 starting...")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("\nThread2 completed.")

def main():
    t1 = threading.Thread(target=Thread1, name="Thread1")
    t2 = threading.Thread(target=Thread2, name="Thread2")
    
    t1.start()
    # Enforce synchronization: Thread2 starts only after Thread1 completes
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
