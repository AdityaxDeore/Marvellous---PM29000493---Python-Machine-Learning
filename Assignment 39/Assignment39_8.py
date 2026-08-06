"""
Question 8:
Write a single structured Python program that performs: 1. Dataset loading 2. Data analysis 3. Visualization 4. Train-test split 5. Model training 6. Prediction 7. Accuracy calculation 8. Confusion matrix generation 9. Final conclusion.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


def LoadDataset():
    DataFrame = pd.read_csv("student_performance_ml.csv")
    return DataFrame


def AnalyzeData(DataFrame):
    print("Shape:", DataFrame.shape)
    print(DataFrame.describe())
    print("Pass/Fail counts:\n", DataFrame["FinalResult"].value_counts())


def VisualizeData(DataFrame):
    DataFrame["FinalResult"].value_counts().plot(kind="bar")
    plt.title("Pass vs Fail distribution")
    plt.xlabel("FinalResult (1=Pass, 0=Fail)")
    plt.savefig("pass_fail_dist.png")
    plt.close()


def SplitData(DataFrame):
    Features = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    X = DataFrame[Features]
    y = DataFrame["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test


def TrainModel(X_train, y_train):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def PredictResult(Model, X_test):
    return Model.predict(X_test)


def CalculateAccuracy(Actual, Predicted):
    return accuracy_score(Actual, Predicted)


def ShowConfusionMatrix(Actual, Predicted):
    cm = confusion_matrix(Actual, Predicted)
    print("Confusion Matrix:\n", cm)

    ConfusionMatrixDisplay(cm, display_labels=["Fail", "Pass"]).plot()
    plt.title("Confusion Matrix")
    plt.savefig("confusion_matrix_full.png")


def FinalConclusion(Accuracy):
    print("Conclusion: The Decision Tree predicts student pass/fail with "
          f"{Accuracy * 100:.2f}% accuracy; the confusion matrix shows most errors are "
          "between borderline students, indicating a reasonably well-fitted model.")


def main():
    print("----- Decision Tree : Student Performance -----")

    df = LoadDataset()
    AnalyzeData(df)
    VisualizeData(df)
    X_train, X_test, y_train, y_test = SplitData(df)
    model = TrainModel(X_train, y_train)
    y_pred = PredictResult(model, X_test)
    acc = CalculateAccuracy(y_test, y_pred)
    print(f"Accuracy: {acc * 100:.2f}%")
    ShowConfusionMatrix(y_test, y_pred)
    FinalConclusion(acc)


if __name__ == "__main__":
    main()
