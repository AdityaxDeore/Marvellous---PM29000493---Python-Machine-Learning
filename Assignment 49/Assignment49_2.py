"""
Question 2:
Write a Python program that calculates the variance and standard deviation
of the dataset:
[6, 7, 8, 9, 10, 11, 12]
Display both results.

Expected Output: Variance: 4.0, Standard Deviation: 2.0
"""

import numpy as np


def CalculateVariance(Data):
    # population variance (ddof=0, divides by N)
    return np.var(Data)


def CalculateStd(Data):
    # population standard deviation (ddof=0)
    return np.std(Data)


def main():
    print("----- Calculate Variance and Standard Deviation -----")

    data = np.array([6, 7, 8, 9, 10, 11, 12])

    variance = CalculateVariance(data)
    std = CalculateStd(data)

    print("Dataset:", data)
    print("Variance:", variance)
    print("Standard Deviation:", std)


if __name__ == "__main__":
    main()
