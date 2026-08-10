"""
Question 4:
Create a NumPy array of 20 random integers between 1 and 100 using
np.random.randint(). Perform the following operations:
- Find the mean, median and standard deviation.
- Find the minimum and maximum values.
- Replace all values less than 50 with 0.
- Count how many values are greater than 75.

Note: Use NumPy statistical functions like mean(), median(), std(), min(), max().
"""

import numpy as np


def CreateArray():
    np.random.seed(42)
    arr = np.random.randint(1, 101, 20)
    return arr


def DisplayStats(Array):
    print("Array:", Array)

    print("\nMean:", Array.mean())
    print("Median:", np.median(Array))
    print("Standard Deviation:", Array.std())
    print("Minimum:", Array.min())
    print("Maximum:", Array.max())

    Array[Array < 50] = 0
    print("\nAfter replacing values less than 50 with 0:", Array)

    count = np.sum(Array > 75)
    print("\nCount of values greater than 75:", count)


def main():
    arr = CreateArray()
    DisplayStats(arr)


if __name__ == "__main__":
    main()
