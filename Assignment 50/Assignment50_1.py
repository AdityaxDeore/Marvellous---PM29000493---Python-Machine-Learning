"""
Question:
Breast Cancer Prediction.
Develop a machine learning model that can accurately predict whether a
tumor is Malignant (harmful) or Benign (non-harmful) based on the given
features. Use load_breast_cancer() method from sklearn to load the dataset.

Objectives:
1. Load and explore the dataset.
2. Perform data preprocessing steps: handle missing values, scale features.
3. Perform exploratory data analysis (EDA): summary statistics,
   visualization of feature correlations.
4. Split the dataset into training and testing sets.
5. Build a machine learning classification model to predict tumor type.
6. Evaluate the model using: Accuracy, Confusion Matrix,
   Precision, Recall, F1-Score.
7. Provide your observations and conclusions.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, f1_score, precision_score,
                             recall_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def LoadDataset():
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="target")
    return data, X, y


def ExploreDataset(Data, X, Y):
    print("Shape:", X.shape)
    print("Target names:", Data.target_names, "(0 = Malignant, 1 = Benign)")
    print("Class balance:\n", Y.value_counts())


def PreprocessData(X):
    print("Missing values:", X.isna().sum().sum())
    scaler = StandardScaler()
    Xs = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    return Xs


def DoEDA(Data, X, Y):
    print(X.describe().T[["mean", "std", "min", "max"]])

    corr_target = X.corrwith(Y).abs().sort_values(ascending=False)
    top = corr_target.head(10).index
    print("Top 10 features by |correlation| with target:\n",
          corr_target.head(10))

    plt.figure(figsize=(8, 6))
    plt.imshow(X[top].corr(), cmap="coolwarm", vmin=-1, vmax=1)
    plt.xticks(range(10), top, rotation=90, fontsize=7)
    plt.yticks(range(10), top, fontsize=7)
    plt.colorbar()
    plt.title("Correlation heatmap (top 10 features)")
    plt.tight_layout()
    plt.savefig("breast_cancer_corr.png")
    plt.close()

    plt.figure()
    Y.value_counts().plot(kind="bar")
    plt.xticks([0, 1], ["Malignant", "Benign"], rotation=0)
    plt.title("Class distribution")
    plt.tight_layout()
    plt.savefig("breast_cancer_classes.png")
    plt.close()


def SplitData(X, Y):
    return train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)


def TrainModel(XTrain, YTrain):
    # RandomForestClassifier - robust default for tabular medical data,
    # captures non-linear feature interactions, resistant to overfitting.
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(XTrain, YTrain)
    return model


def EvaluateModel(Model, XTest, YTest, TargetNames):
    y_pred = Model.predict(XTest)
    acc = accuracy_score(YTest, y_pred)
    cm = confusion_matrix(YTest, y_pred)

    print(f"Accuracy: {acc:.4f}")
    print("Confusion Matrix:\n", cm)
    print(f"Precision: {precision_score(YTest, y_pred):.4f}")
    print(f"Recall: {recall_score(YTest, y_pred):.4f}")
    print(f"F1-Score: {f1_score(YTest, y_pred):.4f}")
    print(classification_report(YTest, y_pred, target_names=TargetNames))
    return acc


def ShowConclusions(Accuracy):
    print("Observations: worst concave points, worst perimeter and mean concave")
    print("points correlate most strongly with malignancy. The Random Forest")
    print("model separates benign from malignant tumors with high accuracy,")
    print(f"achieving {Accuracy:.2%} test accuracy, supporting its use as an")
    print("early-detection aid alongside clinical diagnosis.")


def main():
    print("----- Breast Cancer Prediction -----")

    data, X, y = LoadDataset()
    ExploreDataset(data, X, y)

    Xs = PreprocessData(X)
    DoEDA(data, X, y)

    x_train, x_test, y_train, y_test = SplitData(Xs, y)
    model = TrainModel(x_train, y_train)

    accuracy = EvaluateModel(model, x_test, y_test, data.target_names)
    ShowConclusions(accuracy)

    print("Saved: breast_cancer_corr.png, breast_cancer_classes.png")


if __name__ == "__main__":
    main()
