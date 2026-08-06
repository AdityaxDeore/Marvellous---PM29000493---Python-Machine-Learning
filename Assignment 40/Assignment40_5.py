"""
Question 5:
Without using accuracy_score, manually calculate accuracy. Verify whether it matches sklearn accuracy.
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
    model = DecisionTreeClassifier(random_state=42)
    model.fit(XTrain, YTrain)
    return model


def CalculateManualAccuracy(YTest, YPred):
    return (YTest.values == YPred).mean()


def main():
    print("----- Decision Tree : Manual Accuracy Check -----")

    data_frame = LoadDataset()
    x_train, x_test, y_train, y_test = SplitData(data_frame)
    model = TrainModel(x_train, y_train)

    y_pred = model.predict(x_test)

    manual_acc = CalculateManualAccuracy(y_test, y_pred)
    sklearn_acc = accuracy_score(y_test, y_pred)

    print(f"Manual accuracy : {manual_acc * 100:.2f}%")
    print(f"sklearn accuracy: {sklearn_acc * 100:.2f}%")
    print("Match:", abs(manual_acc - sklearn_acc) < 1e-9)


if __name__ == "__main__":
    main()
