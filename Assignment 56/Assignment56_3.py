"""
Question 3:
Fraudulent Transaction Detection.

A financial institution wants to detect potentially fraudulent transactions.
Target: 0 -> Normal Transaction, 1 -> Fraudulent Transaction.

Build and compare the following model:
3. Random Forest Classifier

Evaluate the model using:
Accuracy, Precision, Recall, F1 Score, Confusion Matrix.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix)


def LoadDataset(FileName):
    df = pd.read_csv(FileName)
    X = df.drop("Fraud", axis=1)
    y = df["Fraud"]
    return X, y


def SplitData(X, y):
    return train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)


def TrainRandomForest(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def EvaluateModel(Model, X_test, y_test, ModelName):
    y_pred = Model.predict(X_test)

    print(ModelName)
    print("Accuracy :", round(accuracy_score(y_test, y_pred), 4))
    print("Precision:", round(precision_score(y_test, y_pred, zero_division=0), 4))
    print("Recall   :", round(recall_score(y_test, y_pred, zero_division=0), 4))
    print("F1 Score :", round(f1_score(y_test, y_pred, zero_division=0), 4))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


def main():
    print("----- Fraudulent Transaction Detection -----")

    X, y = LoadDataset("Fraudulent_Transaction_Detection.csv")
    X_train, X_test, y_train, y_test = SplitData(X, y)

    model = TrainRandomForest(X_train, y_train)
    EvaluateModel(model, X_test, y_test, "Random Forest Classifier")


if __name__ == "__main__":
    main()
