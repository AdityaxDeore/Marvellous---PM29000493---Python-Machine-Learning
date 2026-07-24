"""
Question 4:
Write a program which accepts two file names through command line arguments and compares the contents of both files.
* If both files contain the same contents, display Success.
* Otherwise, display Failure.

Input (Command Line): Demo.txt Hello.txt
Expected Output: Success OR Failure
"""

import sys
import os

def CompareFiles(File1, File2):
    if not os.path.exists(File1) or not os.path.exists(File2):
        print("Failure")
        return
    
    with open(File1, 'r') as f1, open(File2, 'r') as f2:
        if f1.read() == f2.read():
            print("Success")
        else:
            print("Failure")

def main():
    if len(sys.argv) < 3:
        print("Usage: python Ass29_4.py <File1> <File2>")
        return
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    CompareFiles(file1, file2)

if __name__ == "__main__":
    main()
