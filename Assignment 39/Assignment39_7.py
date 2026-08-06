"""
Question 7:
Use the trained model to predict result for a student with: StudyHours = 6, Attendance = 85, PreviousScore = 66, AssignmentsCompleted = 7, SleepHours = 7. Will the student Pass or Fail?
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


def PredictStudent(Model):
    new_student = pd.DataFrame([[6, 85, 66, 7, 7]],
                               columns=["StudyHours", "Attendance", "PreviousScore",
                                        "AssignmentsCompleted", "SleepHours"])

    pred = Model.predict(new_student)[0]

    print("Student details: StudyHours=6, Attendance=85, PreviousScore=66, AssignmentsCompleted=7, SleepHours=7")
    print("Predicted Result:", "Pass" if pred == 1 else "Fail")


def main():
    print("----- Decision Tree : Student Performance -----")

    X, y = LoadDataset()
    X_train, X_test, y_train, y_test = SplitData(X, y)
    model = TrainModel(X_train, y_train)

    PredictStudent(model)


if __name__ == "__main__":
    main()
