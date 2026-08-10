"""
Question 1:
Create two 3x3 matrices using NumPy and perform the following operations:
- Element-wise addition
- Element-wise subtraction
- Element-wise multiplication
- Element-wise division
- Matrix multiplication (dot product)

Note: NumPy supports element-wise and matrix operations using +, -, *, /
and dot() / @ operator.
"""

import numpy as np


def CreateMatrices():
    matrix_a = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

    matrix_b = np.array([[9, 8, 7],
                         [6, 5, 4],
                         [3, 2, 1]])

    return matrix_a, matrix_b


def DisplayOperations(MatrixA, MatrixB):
    print("Matrix A:\n", MatrixA)
    print("Matrix B:\n", MatrixB)

    print("\nElement-wise Addition (A + B):\n", MatrixA + MatrixB)
    print("\nElement-wise Subtraction (A - B):\n", MatrixA - MatrixB)
    print("\nElement-wise Multiplication (A * B):\n", MatrixA * MatrixB)
    print("\nElement-wise Division (A / B):\n", MatrixA / MatrixB)

    print("\nMatrix Multiplication (A dot B):\n", MatrixA.dot(MatrixB))
    print("\nMatrix Multiplication (A @ B):\n", MatrixA @ MatrixB)


def main():
    matrix_a, matrix_b = CreateMatrices()
    DisplayOperations(matrix_a, matrix_b)


if __name__ == "__main__":
    main()
