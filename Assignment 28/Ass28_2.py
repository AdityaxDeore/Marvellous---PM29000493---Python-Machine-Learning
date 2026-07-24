"""
Question 2:
Write a program which accepts a file name from the user and counts the total number of words in that file.

Input: Demo.txt
Expected Output: Total number of words in Demo.txt.
"""

import os

def CountWords(FileName):
    if not os.path.exists(FileName):
        print(f"File '{FileName}' does not exist.")
        return
    
    word_count = 0
    with open(FileName, 'r') as file:
        for line in file:
            words = line.split()
            word_count += len(words)
            
    print(f"Total number of words in '{FileName}': {word_count}")

def main():
    file_name = input("Enter the file name: ")
    CountWords(file_name)

if __name__ == "__main__":
    main()
