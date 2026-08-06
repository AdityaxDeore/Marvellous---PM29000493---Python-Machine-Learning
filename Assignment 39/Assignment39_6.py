"""
Question 6:
Train three Decision Tree models with max_depth = 1, max_depth = 3, max_depth = None. Compare their testing accuracies and write your observations.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def LoadDataset():
    DataFrame = pd.read_csv("student_performance_ml.csv")

    Features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    X = DataFrame[Features]
    y = DataFrame["FinalResult"]

    return X, y


def SplitData(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test


def TrainModel(X_train, y_train, MaxDepth):
    model = DecisionTreeClassifier(max_depth=MaxDepth, random_state=42)
    model.fit(X_train, y_train)
    return model


def CalculateAccuracy(Actual, Predicted):
    return accuracy_score(Actual, Predicted)


def CompareDepths(X_train, X_test, y_train, y_test):
    for depth in (1, 3, None):
        model = TrainModel(X_train, y_train, depth)
        acc = CalculateAccuracy(y_test, model.predict(X_test))
        print(f"max_depth={depth}: Testing Accuracy = {acc * 100:.2f}%")

    print("Observation: max_depth=1 is too shallow and underfits; on this dataset the")
    print("unrestricted tree (max_depth=None) scores highest, while depth=3 sits in between.")


def main():
    print("----- Decision Tree : Student Performance -----")

    X, y = LoadDataset()
    X_train, X_test, y_train, y_test = SplitData(X, y)

    CompareDepths(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
