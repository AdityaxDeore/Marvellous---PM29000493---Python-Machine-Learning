"""
Question 3:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

Input: Demo.txt
Expected Output: Display each line of Demo.txt one by one.
"""

import os

def DisplayLineByLine(FileName):
    if not os.path.exists(FileName):
        print(f"File '{FileName}' does not exist.")
        return
    
    with open(FileName, 'r') as file:
        for line in file:
            print(line, end='')
    print()

def main():
    file_name = input("Enter the file name: ")
    DisplayLineByLine(file_name)

if __name__ == "__main__":
    main()
