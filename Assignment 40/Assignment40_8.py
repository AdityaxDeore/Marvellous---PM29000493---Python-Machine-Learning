"""
Question 8:
Decision Tree Visualization. Use from sklearn.tree import plot_tree. Visualize the trained decision tree. Which feature appears at the root node? Why do you think that feature was selected first?
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree


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


def ShowTree(Model, Features):
    root_feature = Features[Model.tree_.feature[0]]
    print("Root node feature:", root_feature)
    print("Reason: The root split is chosen to maximize information gain (impurity reduction);")
    print("it is the feature that best separates Pass from Fail at the first split.")

    plt.figure(figsize=(16, 10))
    plot_tree(Model, feature_names=Features, class_names=["Fail", "Pass"], filled=True)
    plt.title("Decision Tree Visualization")
    plt.savefig("tree_viz.png")
    print("Saved tree_viz.png")


def main():
    print("----- Decision Tree : Visualization -----")

    features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

    data_frame = LoadDataset()
    x_train, x_test, y_train, y_test = SplitData(data_frame)
    model = TrainModel(x_train, y_train)

    ShowTree(model, features)


if __name__ == "__main__":
    main()
