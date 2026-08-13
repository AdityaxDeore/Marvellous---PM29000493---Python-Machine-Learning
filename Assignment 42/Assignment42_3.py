"""
Question 3:
Use KNN to predict whether a student passes or fails based on study hours
and attendance.

Tasks:
1. Accept input from user:
   - Study hours
   - Attendance percentage
2. Apply KNN algorithm.
3. Predict whether the student Passes or Fails.

Input Example:
Enter Study Hours: 4
Enter Attendance: 70

Expected Output:
Predicted Result: Pass
"""

import math


def EuclideanDistance(Point1, Point2):
    x1, y1 = Point1
    x2, y2 = Point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def GetNeighbors(Data, NewPoint, K):
    distances = []
    for hours, attendance, result in Data:
        d = EuclideanDistance(NewPoint, (hours, attendance))
        distances.append((d, result))

    distances.sort(key=lambda t: t[0])
    return distances[:K]


def PredictResult(Neighbors):
    votes = {}
    for d, result in Neighbors:
        votes[result] = votes.get(result, 0) + 1
    return max(votes, key=lambda r: votes[r])


def main():
    data = [(2, 60, "Fail"), (5, 80, "Pass"),
            (6, 85, "Pass"), (1, 50, "Fail")]

    hours = float(input("Enter Study Hours: "))
    attendance = float(input("Enter Attendance: "))

    neighbors = GetNeighbors(data, (hours, attendance), 3)
    print("Predicted Result: " + PredictResult(neighbors))


if __name__ == "__main__":
    main()
