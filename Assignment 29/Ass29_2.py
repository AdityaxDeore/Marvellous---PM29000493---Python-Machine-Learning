"""
Question 2:
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

Input: Demo.txt
Expected Output: Display contents of Demo.txt on the console.
"""

import os

def DisplayFileContents(FileName):
    if not os.path.exists(FileName):
        print(f"File '{FileName}' does not exist.")
        return
    
    with open(FileName, 'r') as file:
        content = file.read()
        print(content)

def main():
    file_name = input("Enter the file name: ")
    DisplayFileContents(file_name)

if __name__ == "__main__":
    main()
