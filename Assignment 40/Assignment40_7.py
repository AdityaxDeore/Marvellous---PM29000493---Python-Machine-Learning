"""
Question 7:
Train model using random_state = 0, random_state = 10, random_state = 42. Compare testing accuracy. Does the result change?
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def LoadDataset():
    return pd.read_csv("student_performance_ml.csv")


def SplitData(DataFrame, RandomState):
    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    X = DataFrame[features]
    y = DataFrame["FinalResult"]
    return train_test_split(X, y, test_size=0.3, random_state=RandomState)


def TrainModel(XTrain, YTrain):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(XTrain, YTrain)
    return model


def CalculateAccuracy(Model, XTest, YTest):
    return accuracy_score(YTest, Model.predict(XTest))


def main():
    print("----- Decision Tree : random_state Comparison -----")

    data_frame = LoadDataset()

    for rs in (0, 10, 42):
        x_train, x_test, y_train, y_test = SplitData(data_frame, rs)
        model = TrainModel(x_train, y_train)
        accuracy = CalculateAccuracy(model, x_test, y_test)
        print(f"random_state={rs}: Testing Accuracy = {accuracy * 100:.2f}%")

    print("Conclusion: Yes, the result changes because a different random_state creates a different")
    print("train/test split, and the decision tree learns from different training samples.")


if __name__ == "__main__":
    main()
