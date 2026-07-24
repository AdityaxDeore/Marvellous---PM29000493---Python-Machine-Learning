"""
Question 5:
Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

Input: Demo.txt Marvellous
Expected Output: Display whether the word Marvellous is found in Demo.txt or not.
"""

import os

def SearchWord(FileName, TargetWord):
    if not os.path.exists(FileName):
        print(f"File '{FileName}' does not exist.")
        return
    
    found = False
    with open(FileName, 'r') as file:
        for line in file:
            words = line.split()
            if TargetWord in words:
                found = True
                break
                
    if found:
        print(f"The word '{TargetWord}' is present in '{FileName}'.")
    else:
        print(f"The word '{TargetWord}' is not present in '{FileName}'.")

def main():
    file_name = input("Enter the file name: ")
    search_word = input("Enter the word to search: ")
    SearchWord(file_name, search_word)

if __name__ == "__main__":
    main()
