"""
Question 2:
The value of K plays an important role in the KNN algorithm. Write a Python
program that demonstrates how prediction changes when K changes. Use the same
dataset as Question 1. Predict the class of the same new point using:
- K = 1
- K = 5

Prediction Results:
K = 1 -> Red
K = 3 -> Red
K = 5 -> Blue

Explain why the prediction changes when K increases.
"""

import math


def EuclideanDistance(Point1, Point2):
    x1, y1 = Point1
    x2, y2 = Point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def PredictClass(Data, NewPoint, K):
    distances = []
    for name, px, py, label in Data:
        d = EuclideanDistance(NewPoint, (px, py))
        distances.append((d, name, label))

    distances.sort(key=lambda t: t[0])
    neighbors = distances[:K]

    votes = {}
    for d, name, label in neighbors:
        votes[label] = votes.get(label, 0) + 1

    # Tie-break: class of the farthest neighbor among the K selected
    if len(votes) == 1:
        return neighbors[0][2]

    highest = max(votes.values())
    tied = [l for l, c in votes.items() if c == highest]
    if len(tied) == 1:
        return tied[0]
    return neighbors[-1][2]


def main():
    data = [("A", 1, 2, "Red"), ("B", 2, 3, "Red"),
            ("C", 3, 1, "Blue"), ("D", 6, 5, "Blue")]
    new_point = (2, 2)

    for k in (1, 3, 5):
        print("K = " + str(k) + " -> " + PredictClass(data, new_point, k))

    print()
    print("Why the prediction changes when K increases:")
    print("K = 1 uses only the single nearest point (A, Red).")
    print("K = 3 uses the 3 nearest points (A, B are Red and C is Blue) so majority is Red.")
    print("K = 5 is larger than the dataset, so all 4 points vote: 2 Red and 2 Blue.")
    print("The tie is broken by the farthest neighbor (D, Blue),")
    print("so a large K lets the distant Blue points change the prediction.")


if __name__ == "__main__":
    main()
