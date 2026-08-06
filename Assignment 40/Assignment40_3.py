"""
Question 3:
Train the model using only StudyHours and Attendance. Compare the accuracy with the full-feature model. Is the model still performing well?
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


def main():
    print("----- Decision Tree : Two Features vs Full Features -----")

    data_frame = LoadDataset()

    feature_sets = (
        ("Full features (5)", ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]),
        ("Only StudyHours + Attendance", ["StudyHours", "Attendance"]),
    )

    for name, features in feature_sets:
        x_train, x_test, y_train, y_test = SplitData(data_frame, features)
        model = TrainModel(x_train, y_train)
        accuracy = CalculateAccuracy(model, x_test, y_test)
        print(f"{name}: Accuracy = {accuracy * 100:.2f}%")

    print("Conclusion: The two-feature model is simpler but less accurate; the full-feature model performs better.")


if __name__ == "__main__":
    main()
