"""
Question 6:
Write a Python program using NumPy to:
a) Create an array of training points.
b) Calculate distances of a new point from all training points.
c) Print the index of the closest training point.
"""

import numpy as np


def CalculateDistances(NewPoint, TrainingPoints):
    return np.sqrt(np.sum((TrainingPoints - NewPoint) ** 2, axis=1))


def FindClosestIndex(Distances):
    return np.argmin(Distances)


def main():
    print("----- Find Closest Training Point -----")

    training_points = np.array([[2, 3], [3, 4], [4, 3],
                                [7, 8], [8, 7], [6, 9]])
    new_point = np.array([5, 5])

    distances = CalculateDistances(new_point, training_points)
    print("Distances:", distances)

    closest = FindClosestIndex(distances)
    print("Index of closest training point:", closest)


if __name__ == "__main__":
    main()
