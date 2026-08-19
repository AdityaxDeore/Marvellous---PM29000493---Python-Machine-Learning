"""
Question 3:
Write a Python program using StandardScaler to perform feature scaling on
the following dataset:
[[25,20000],
 [30,40000],
 [35,80000]]
Print the scaled dataset.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler


def CreateDataset():
    return np.array([[25, 20000],
                     [30, 40000],
                     [35, 80000]])


def ScaleFeatures(Data):
    scaler = StandardScaler()
    return scaler.fit_transform(Data)


def main():
    print("----- Feature Scaling with StandardScaler -----")

    data = CreateDataset()
    scaled = ScaleFeatures(data)

    print("Original dataset:")
    print(data)
    print("\nScaled dataset:")
    print(scaled)


if __name__ == "__main__":
    main()
