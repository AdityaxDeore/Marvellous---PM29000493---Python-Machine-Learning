"""
Question 2:
Create a NumPy array of numbers from 1 to 15. Perform the following operations:
- Reshape it into a 3x5 matrix.
- Replace all numbers greater than 10 with 0.
- Find the transpose of the resulting matrix.
- Save the final matrix to a text file using np.savetxt().
- Load the matrix back using np.loadtxt().

Note: Use np.savetxt() and np.loadtxt() for file handling.
"""

import numpy as np


def CreateMatrix():
    arr = np.arange(1, 16)
    matrix = arr.reshape(3, 5)
    return matrix


def SaveMatrix(Matrix, FileName):
    try:
        np.savetxt(FileName, Matrix)
        print("\nMatrix saved to " + FileName)
    except OSError:
        print("File cannot be written")


def LoadMatrix(FileName):
    try:
        return np.loadtxt(FileName)
    except OSError:
        print("File cannot be opened")
        return None


def main():
    matrix = CreateMatrix()
    print("3x5 Matrix:\n", matrix)

    matrix[matrix > 10] = 0
    print("\nAfter replacing values greater than 10 with 0:\n", matrix)

    transposed = matrix.T
    print("\nTranspose:\n", transposed)

    file_name = "matrix.txt"
    SaveMatrix(transposed, file_name)

    loaded = LoadMatrix(file_name)
    if loaded is not None:
        print("\nMatrix loaded back from file:\n", loaded)


if __name__ == "__main__":
    main()
