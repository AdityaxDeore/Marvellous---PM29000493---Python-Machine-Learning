"""
Question 5:
Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

Input: Demo.txt Marvellous
Expected Output: Count how many times "Marvellous" appears in Demo.txt.
"""

import os

def FrequencyOfString(FileName, SearchString):
    if not os.path.exists(FileName):
        print(f"File '{FileName}' does not exist.")
        return 0
    
    with open(FileName, 'r') as file:
        content = file.read()
        count = content.count(SearchString)
        
    print(f"Frequency of '{SearchString}' in '{FileName}': {count}")
    return count

def main():
    file_name = input("Enter the file name: ")
    search_str = input("Enter the string to search: ")
    FrequencyOfString(file_name, search_str)

if __name__ == "__main__":
    main()
