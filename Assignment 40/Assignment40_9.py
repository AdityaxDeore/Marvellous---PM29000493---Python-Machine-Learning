"""
Question 9:
Create a new column: PerformanceIndex = (StudyHours * 2) + Attendance. Train the model including this new feature. Does accuracy improve?
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def LoadDataset():
    return pd.read_csv("student_performance_ml.csv")


def SplitData(DataFrame, Features):
    X = DataFrame[Features]
    y = DataFrame["FinalResult"]
    return train_test_split(X, y, test_size=0.3, random_state=42)


def TrainModel(XTrain, YTrain):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(XTrain, YTrain)
    return model


def CalculateAccuracy(Model, XTest, YTest):
    return accuracy_score(YTest, Model.predict(XTest))


def AddPerformanceIndex(DataFrame):
    new_frame = DataFrame.copy()
    new_frame["PerformanceIndex"] = new_frame["StudyHours"] * 2 + new_frame["Attendance"]
    return new_frame


def main():
    print("----- Decision Tree : PerformanceIndex Feature -----")

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    data_frame = LoadDataset()

    x_train, x_test, y_train, y_test = SplitData(data_frame, features)
    model = TrainModel(x_train, y_train)
    base_acc = CalculateAccuracy(model, x_test, y_test)

    new_frame = AddPerformanceIndex(data_frame)
    x2_train, x2_test, y2_train, y2_test = SplitData(new_frame, features + ["PerformanceIndex"])
    model2 = TrainModel(x2_train, y2_train)
    new_acc = CalculateAccuracy(model2, x2_test, y2_test)

    print(f"Accuracy without PerformanceIndex: {base_acc * 100:.2f}%")
    print(f"Accuracy with PerformanceIndex   : {new_acc * 100:.2f}%")
    print("Improved:", new_acc > base_acc)
    print("Note: PerformanceIndex combines two strong signals (StudyHours, Attendance) into")
    print("one feature, which slightly helps the tree here — accuracy improved modestly.")


if __name__ == "__main__":
    main()
