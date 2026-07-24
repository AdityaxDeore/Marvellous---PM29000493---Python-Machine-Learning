"""
Question 1:
Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

Input: Demo.txt
Expected Output: Display whether Demo.txt exists or not.
"""

import os

def CheckFileExists(FileName):
    if os.path.exists(FileName):
        print(f"File '{FileName}' exists in the current directory.")
    else:
        print(f"File '{FileName}' does NOT exist in the current directory.")

def main():
    file_name = input("Enter the file name: ")
    CheckFileExists(file_name)

if __name__ == "__main__":
    main()
