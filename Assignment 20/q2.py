# Design a Python application that creates two threads named EvenFactor and OddFactor. Both threads should accept one integer number as a parameter. The EvenFactor thread should identify all even factors of the given number and calculate and display their sum. The OddFactor thread should identify all odd factors of the given number and calculate and display their sum. After both threads complete execution, the main thread should display the message "Exit from main".

import threading

def EvenFactor(number):
    total = 0
    factors = []
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 == 0:
            factors.append(i)
            total += i
    print(f"EvenFactor Thread: Even factors of {number} are {factors}, Sum = {total}")

def OddFactor(number):
    total = 0
    factors = []
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 != 0:
            factors.append(i)
            total += i
    print(f"OddFactor Thread: Odd factors of {number} are {factors}, Sum = {total}")

def main():
    val = int(input("Enter a number: "))
    
    t1 = threading.Thread(target=EvenFactor, args=(val,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(val,), name="OddFactor")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Exit from main")

if __name__ == "__main__":
    main()
