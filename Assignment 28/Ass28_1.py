"""
Question 1:
Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input: Demo.txt
Expected Output: Total number of lines in Demo.txt.
"""

import os

def CountLines(FileName):
    if not os.path.exists(FileName):
        print(f"File '{FileName}' does not exist.")
        return
    
    count = 0
    with open(FileName, 'r') as file:
        for _ in file:
            count += 1
            
    print(f"Total number of lines in '{FileName}': {count}")

def main():
    file_name = input("Enter the file name: ")
    CountLines(file_name)

if __name__ == "__main__":
    main()
