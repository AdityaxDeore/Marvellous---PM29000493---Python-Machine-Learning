# Design a Python application that creates three threads named Small, Capital, and Digits. All threads should accept a string as input. The Small thread should count and display the number of lowercase characters. The Capital thread should count and display the number of uppercase characters. The Digits thread should count and display the number of numeric digits. Each thread must also display Thread ID and Thread Name.

import threading

def Small(s):
    count = sum(1 for c in s if c.islower())
    print(f"Thread Name: {threading.current_thread().name}, ID: {threading.get_ident()}")
    print(f"Small Thread: Number of lowercase characters = {count}\n")

def Capital(s):
    count = sum(1 for c in s if c.isupper())
    print(f"Thread Name: {threading.current_thread().name}, ID: {threading.get_ident()}")
    print(f"Capital Thread: Number of uppercase characters = {count}\n")

def Digits(s):
    count = sum(1 for c in s if c.isdigit())
    print(f"Thread Name: {threading.current_thread().name}, ID: {threading.get_ident()}")
    print(f"Digits Thread: Number of numeric digits = {count}\n")

def main():
    user_string = input("Enter a string: ")
    
    t1 = threading.Thread(target=Small, args=(user_string,), name="Small")
    t2 = threading.Thread(target=Capital, args=(user_string,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(user_string,), name="Digits")
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
