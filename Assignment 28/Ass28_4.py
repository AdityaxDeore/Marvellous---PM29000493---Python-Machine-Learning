"""
Question 4:
Write a program which accepts two file names from the user.
* First file is an existing file
* Second file is a new file
Copy all contents from the first file into the second file.

Input: ABC.txt Demo.txt
Expected Output: Contents of ABC.txt copied into Demo.txt.
"""

import os

def CopyFile(SourceFile, DestFile):
    if not os.path.exists(SourceFile):
        print(f"Source file '{SourceFile}' does not exist.")
        return
    
    with open(SourceFile, 'r') as s_file, open(DestFile, 'w') as d_file:
        for line in s_file:
            d_file.write(line)
            
    print(f"Contents of '{SourceFile}' copied into '{DestFile}'.")

def main():
    source = input("Enter the existing file name: ")
    dest = input("Enter the new file name: ")
    CopyFile(source, dest)

if __name__ == "__main__":
    main()
