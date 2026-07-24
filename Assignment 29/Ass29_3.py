"""
Question 3:
Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.

Input (Command Line): ABC.txt
Expected Output: Create Demo.txt and copy contents of ABC.txt into Demo.txt.
"""

import sys
import os

def CopyToDemo(SourceFile):
    if not os.path.exists(SourceFile):
        print(f"File '{SourceFile}' does not exist.")
        return
    
    dest_file = "Demo.txt"
    with open(SourceFile, 'r') as s_file, open(dest_file, 'w') as d_file:
        content = s_file.read()
        d_file.write(content)
        
    print(f"Contents of '{SourceFile}' successfully copied into '{dest_file}'.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python Ass29_3.py <SourceFileName>")
        return
    
    source_file = sys.argv[1]
    CopyToDemo(source_file)

if __name__ == "__main__":
    main()
