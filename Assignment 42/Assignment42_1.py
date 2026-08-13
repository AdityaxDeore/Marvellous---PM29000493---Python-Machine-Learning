"""
Question 1:
Write a Python program that classifies a new data point using the K-Nearest
Neighbors algorithm. The algorithm should be implemented manually without
using any machine learning library. The program should:
- Calculate Euclidean distance
- Sort distances
- Select K nearest neighbors
- Predict the class based on majority voting.

Tasks:
1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K = 3 nearest neighbors.
5. Predict the class label.

Input:
Enter X coordinate: 2
Enter Y coordinate: 2

Expected Output:
A - Distance: 1.0
B - Distance: 1.0
C - Distance: 1.41
Predicted Class: Red
"""

import math


def EuclideanDistance(Point1, Point2):
    x1, y1 = Point1
    x2, y2 = Point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def GetNeighbors(Data, NewPoint, K):
    distances = []
    for name, px, py, label in Data:
        d = EuclideanDistance(NewPoint, (px, py))
        distances.append((d, name, label))

    distances.sort(key=lambda t: t[0])
    return distances[:K]


def PredictClass(Neighbors):
    votes = {}
    for d, name, label in Neighbors:
        votes[label] = votes.get(label, 0) + 1
    return max(votes, key=lambda l: votes[l])


def main():
    data = [("A", 1, 2, "Red"), ("B", 2, 3, "Red"),
            ("C", 3, 1, "Blue"), ("D", 6, 5, "Blue")]

    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    neighbors = GetNeighbors(data, (x, y), 3)

    for d, name, label in neighbors:
        print(name + " - Distance: " + str(round(d, 2)))

    print("Predicted Class: " + PredictClass(neighbors))


if __name__ == "__main__":
    main()
