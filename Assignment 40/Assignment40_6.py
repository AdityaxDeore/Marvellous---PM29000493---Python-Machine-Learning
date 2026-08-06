"""
Question 6:
Identify students where y_test != y_pred. Display those rows. How many students were misclassified? What common pattern do you observe?
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def LoadDataset():
    return pd.read_csv("student_performance_ml.csv")


def SplitData(DataFrame):
    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    X = DataFrame[features]
    y = DataFrame["FinalResult"]
    return train_test_split(X, y, test_size=0.3, random_state=42)


def TrainModel(XTrain, YTrain):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(XTrain, YTrain)
    return model


def FindMisclassified(XTest, YTest, YPred):
    wrong = YTest.values != YPred
    mis = XTest[wrong].copy()
    mis["Actual"] = YTest.values[wrong]
    mis["Predicted"] = YPred[wrong]
    return mis


def main():
    print("----- Decision Tree : Misclassified Students -----")

    data_frame = LoadDataset()
    x_train, x_test, y_train, y_test = SplitData(data_frame)
    model = TrainModel(x_train, y_train)

    y_pred = model.predict(x_test)
    misclassified = FindMisclassified(x_test, y_test, y_pred)

    print("Misclassified students:")
    print(misclassified.to_string(index=False))
    print("Total misclassified:", len(misclassified))
    print("Pattern: Misclassified students are borderline cases (e.g. low study hours but high attendance/previous score), where feature values conflict.")


if __name__ == "__main__":
    main()
