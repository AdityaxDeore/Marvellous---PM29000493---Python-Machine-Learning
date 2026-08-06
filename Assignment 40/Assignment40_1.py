"""
Question 1:
After training the Decision Tree model, use model.feature_importances_. Display importance score of each feature. Which feature contributes the most in predicting FinalResult? Which feature contributes the least?
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


def ShowFeatureImportance(Model, Features):
    importance = Model.feature_importances_

    for name, score in zip(Features, importance):
        print(f"{name}: {score:.4f}")

    print("Most contributing feature :", Features[importance.argmax()])
    print("Least contributing feature:", Features[importance.argmin()])


def main():
    print("----- Decision Tree : Feature Importance -----")

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    data_frame = LoadDataset()
    x_train, x_test, y_train, y_test = SplitData(data_frame, features)
    model = TrainModel(x_train, y_train)

    ShowFeatureImportance(model, features)


if __name__ == "__main__":
    main()
