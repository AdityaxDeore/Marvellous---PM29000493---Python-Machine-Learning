"""
Question 4:
Write a Python program to calculate the Euclidean distance between two
points before and after applying feature scaling, and explain the
difference in results.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler


def CreateDataset():
    return np.array([[25, 20000],
                     [30, 40000],
                     [35, 80000]])


def CalculateDistance(Point1, Point2):
    return np.linalg.norm(Point1 - Point2)


def ScaleFeatures(Data):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(Data)
    return scaler, scaled


def main():
    print("----- Euclidean Distance Before and After Scaling -----")

    data = CreateDataset()
    point1 = np.array([25, 20000])
    point2 = np.array([35, 80000])

    dist_before = CalculateDistance(point1, point2)
    print("Euclidean distance before scaling:", dist_before)

    scaler, scaled = ScaleFeatures(data)
    sp1 = scaler.transform([point1])[0]
    sp2 = scaler.transform([point2])[0]

    dist_after = CalculateDistance(sp1, sp2)
    print("Euclidean distance after scaling:", dist_after)

    print("\nExplanation: before scaling, the second feature (salary, in tens of thousands)")
    print("dominates the distance calculation and the first feature (age) has almost no")
    print("effect. After scaling, both features contribute equally, so the distance")
    print("reflects differences in both features fairly.")


if __name__ == "__main__":
    main()
