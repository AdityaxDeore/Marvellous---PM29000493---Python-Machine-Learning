"""
Question 2:
Use the trained model to predict results for X_test. Display predicted values along with actual values.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


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


def PredictResult(Model, X_test):
    return Model.predict(X_test)


def DisplayPredictions(Predictions, Actual):
    print("Predicted :", list(Predictions))
    print("Actual    :", list(Actual))

    for p, a in zip(Predictions, Actual):
        print(f"Predicted: {p} ({'Pass' if p == 1 else 'Fail'}) | Actual: {a} ({'Pass' if a == 1 else 'Fail'})")


def main():
    print("----- Decision Tree : Student Performance -----")

    X, y = LoadDataset()
    X_train, X_test, y_train, y_test = SplitData(X, y)
    model = TrainModel(X_train, y_train)

    y_pred = PredictResult(model, X_test)
    DisplayPredictions(y_pred, y_test.values)


if __name__ == "__main__":
    main()
