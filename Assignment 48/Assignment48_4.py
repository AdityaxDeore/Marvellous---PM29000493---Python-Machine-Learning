"""
Question 4:
Write a Python program that:
a) Calculates the Euclidean distance between points (1, 2) and (4, 6).
b) Stores distances of a new point from training points in a list.
c) Sorts the distances to find the nearest neighbors.
"""

import math


def CalculateDistance(Point1, Point2):
    return math.sqrt((Point2[0] - Point1[0]) ** 2 +
                     (Point2[1] - Point1[1]) ** 2)


def CalculateDistances(NewPoint, TrainingPoints):
    distances = []
    for point in TrainingPoints:
        distances.append(CalculateDistance(NewPoint, point))
    return distances


def main():
    print("----- Euclidean Distance and Nearest Neighbors -----")

    distance = CalculateDistance((1, 2), (4, 6))
    print("Distance between (1,2) and (4,6):", distance)

    training_points = [(2, 3), (3, 4), (4, 3), (7, 8), (8, 7), (6, 9)]
    new_point = (5, 5)

    distances = CalculateDistances(new_point, training_points)
    print("Distances:", distances)

    sorted_distances = sorted(distances)
    print("Sorted distances:", sorted_distances)
    print("Nearest neighbor distance:", sorted_distances[0])


if __name__ == "__main__":
    main()
