"""
Question 1:
Write a Python program that calculates the mean of a dataset using NumPy
for the following values:
[6, 7, 8, 9, 10, 11, 12]

Expected Output: Mean: 9.0
"""

import numpy as np


def CalculateMean(Data):
    return np.mean(Data)


def main():
    print("----- Calculate Mean -----")

    data = np.array([6, 7, 8, 9, 10, 11, 12])

    mean = CalculateMean(data)
    print("Dataset:", data)
    print("Mean:", mean)


if __name__ == "__main__":
    main()
