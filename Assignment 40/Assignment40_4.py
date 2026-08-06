"""
Question 4:
Create a new DataFrame with details of 5 new students. Use the trained model to predict their results. Display predictions clearly.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


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


def CreateNewStudents(Features):
    return pd.DataFrame([
        [8, 95, 88, 9, 8.0],
        [2, 55, 40, 2, 5.0],
        [6, 75, 70, 6, 7.0],
        [4, 60, 55, 3, 6.5],
        [9, 98, 92, 10, 7.5],
    ], columns=Features)


def PredictResults(Model, NewStudents):
    predictions = Model.predict(NewStudents)
    NewStudents["PredictedResult"] = ["Pass" if p == 1 else "Fail" for p in predictions]
    return NewStudents


def main():
    print("----- Decision Tree : Predicting New Students -----")

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    data_frame = LoadDataset()
    x_train, x_test, y_train, y_test = SplitData(data_frame, features)
    model = TrainModel(x_train, y_train)

    new_students = CreateNewStudents(features)
    results = PredictResults(model, new_students)

    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
