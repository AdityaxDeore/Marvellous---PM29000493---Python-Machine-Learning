"""
Question 4:
Generate confusion matrix using sklearn. Display it using ConfusionMatrixDisplay. Explain clearly: True Positive, True Negative, False Positive, False Negative.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


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


def ShowConfusionMatrix(Actual, Predicted):
    cm = confusion_matrix(Actual, Predicted)
    print("Confusion Matrix:\n", cm)

    tn, fp, fn, tp = cm.ravel()
    print(f"True Positive (TP): {tp}  - student passed and model predicted pass")
    print(f"True Negative (TN): {tn}  - student failed and model predicted fail")
    print(f"False Positive (FP): {fp} - student failed but model predicted pass")
    print(f"False Negative (FN): {fn} - student passed but model predicted fail")

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fail", "Pass"])
    disp.plot()
    plt.title("Confusion Matrix - Decision Tree")
    plt.savefig("confusion_matrix.png")
    print("Saved confusion_matrix.png")


def main():
    print("----- Decision Tree : Student Performance -----")

    X, y = LoadDataset()
    X_train, X_test, y_train, y_test = SplitData(X, y)
    model = TrainModel(X_train, y_train)

    ShowConfusionMatrix(y_test, model.predict(X_test))


if __name__ == "__main__":
    main()
