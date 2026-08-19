"""
Question 8:
Write a Python program that calculates TP, TN, FP, FN for the following arrays:
actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]
Display all four values.

Expected Output: TP: 3, TN: 3, FP: 1, FN: 1
"""

import numpy as np


def FindConfusionValues(Actual, Predicted):
    tp = np.sum((Actual == 1) & (Predicted == 1))
    tn = np.sum((Actual == 0) & (Predicted == 0))
    fp = np.sum((Actual == 0) & (Predicted == 1))
    fn = np.sum((Actual == 1) & (Predicted == 0))
    return tp, tn, fp, fn


def main():
    print("----- Confusion Matrix Values using NumPy -----")

    actual = np.array([1, 1, 1, 1, 0, 0, 0, 0])
    predicted = np.array([1, 1, 0, 1, 0, 1, 0, 0])

    tp, tn, fp, fn = FindConfusionValues(actual, predicted)

    print("True Positive (TP):", tp)
    print("True Negative (TN):", tn)
    print("False Positive (FP):", fp)
    print("False Negative (FN):", fn)


if __name__ == "__main__":
    main()
