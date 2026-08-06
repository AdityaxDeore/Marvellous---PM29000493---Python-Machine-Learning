"""
Question 5:
Calculate training accuracy and testing accuracy. Compare both and comment whether the model is overfitting or underfitting.
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


def CheckFitting(TrainAccuracy, TestAccuracy):
    print(f"Training Accuracy: {TrainAccuracy * 100:.2f}%")
    print(f"Testing Accuracy : {TestAccuracy * 100:.2f}%")

    if TrainAccuracy > TestAccuracy + 0.10:
        print("Conclusion: Model is OVERFITTING (train accuracy much higher than test accuracy).")
    elif TestAccuracy > TrainAccuracy + 0.10:
        print("Conclusion: Model is UNDERFITTING (both low, test higher than train is unusual).")
    else:
        print("Conclusion: Model is well-fitted (training and testing accuracy are close).")


def main():
    print("----- Decision Tree : Student Performance -----")

    X, y = LoadDataset()
    X_train, X_test, y_train, y_test = SplitData(X, y)
    model = TrainModel(X_train, y_train)

    train_acc = CalculateAccuracy(y_train, model.predict(X_train))
    test_acc = CalculateAccuracy(y_test, model.predict(X_test))
    CheckFitting(train_acc, test_acc)


if __name__ == "__main__":
    main()
