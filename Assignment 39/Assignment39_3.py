"""
Question 3:
Calculate model accuracy using accuracy_score. Display the result in percentage format.
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


def TrainModel(X_train, y_train):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def CalculateAccuracy(Actual, Predicted):
    return accuracy_score(Actual, Predicted)


def main():
    print("----- Decision Tree : Student Performance -----")

    X, y = LoadDataset()
    X_train, X_test, y_train, y_test = SplitData(X, y)
    model = TrainModel(X_train, y_train)

    acc = CalculateAccuracy(y_test, model.predict(X_test))
    print(f"Model Accuracy: {acc * 100:.2f}%")


if __name__ == "__main__":
    main()
