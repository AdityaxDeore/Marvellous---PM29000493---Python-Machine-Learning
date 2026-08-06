"""
Question 10:
Train model with max_depth = None. Display training accuracy and testing accuracy. If training accuracy is 100% but testing accuracy is lower, explain why this happens.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def LoadDataset():
    return pd.read_csv("student_performance_ml.csv")


def SplitData(DataFrame):
    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    X = DataFrame[features]
    y = DataFrame["FinalResult"]
    return train_test_split(X, y, test_size=0.3, random_state=42)


def TrainModel(XTrain, YTrain):
    model = DecisionTreeClassifier(max_depth=None, random_state=42)
    model.fit(XTrain, YTrain)
    return model


def CalculateAccuracy(Model, XData, YData):
    return accuracy_score(YData, Model.predict(XData))


def main():
    print("----- Decision Tree : max_depth = None (Overfitting) -----")

    data_frame = LoadDataset()
    x_train, x_test, y_train, y_test = SplitData(data_frame)
    model = TrainModel(x_train, y_train)

    train_acc = CalculateAccuracy(model, x_train, y_train)
    test_acc = CalculateAccuracy(model, x_test, y_test)

    print(f"Training Accuracy: {train_acc * 100:.2f}%")
    print(f"Testing Accuracy : {test_acc * 100:.2f}%")
    print("Explanation: With max_depth=None the tree grows until every training sample is")
    print("perfectly classified (memorizes noise), so training accuracy is 100%, but unseen")
    print("test data accuracy is lower. This is OVERFITTING — the model learned the training")
    print("data too specifically and generalizes poorly.")


if __name__ == "__main__":
    main()
