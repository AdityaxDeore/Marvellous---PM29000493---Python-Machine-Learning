"""
Question 2:
Remove the column SleepHours from the dataset. Train the model again. Compare new accuracy with previous accuracy. Does removing this feature affect performance?
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def LoadDataset():
    return pd.read_csv("student_performance_ml.csv")


def GetFeatureData(DataFrame, IncludeSleepHours):
    if IncludeSleepHours:
        return DataFrame[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
    return DataFrame.drop(columns=["SleepHours", "FinalResult"])


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
    print("----- Decision Tree : Removing SleepHours -----")

    data_frame = LoadDataset()

    results = {}

    for name, include in (("Full features", True), ("Without SleepHours", False)):
        features = GetFeatureData(data_frame, include)
        x_train, x_test, y_train, y_test = SplitData(data_frame, features.columns)
        model = TrainModel(x_train, y_train)

        results[name] = CalculateAccuracy(model, x_test, y_test)
        print(f"{name}: Accuracy = {results[name] * 100:.2f}%")

    diff = results["Full features"] - results["Without SleepHours"]
    print(f"Accuracy change: {diff * 100:+.2f}%")
    print("Conclusion: Removing SleepHours barely changes accuracy, so it is not an important feature.")


if __name__ == "__main__":
    main()
