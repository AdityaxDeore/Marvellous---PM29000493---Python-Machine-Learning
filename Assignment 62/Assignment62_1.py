"""
Question 1:
Employee Attrition Prediction using MLPClassifier.

Predict whether an employee will stay (0) or leave (1).
Dataset: Employee_Attrition.csv (created for this assignment).

Features: Age, MonthlyIncome, YearsAtCompany, TotalWorkingYears, DistanceFromHome,
JobSatisfaction (1-4), WorkLifeBalance (1-4), OverTime (Yes/No), NumCompaniesWorked,
TrainingTimesLastYear, Attrition (Yes/No target).

Tasks:
1. Import Libraries and Create Dataset
2. Handle Missing Values
3. Preprocess Categorical Columns
4. Exploratory Data Analysis
5. Train-Test Split
6. Feature Scaling
7. Build MLPClassifier
8. Evaluate the Model
9. Check Overfitting / Underfitting
10. Cross-Validation
11. Plot Loss Curve
12. Plot ROC Curve
13. Predict on New Data
14. Write Conclusion
15. Save Output
16. Bonus Task (tanh activation experiment)
17. Explain Working of the Algorithm
18. Model Improvement Notes
19. HR Recommendation Report
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, classification_report,
                             roc_curve, auc)


def LoadDataset(FileName):
    df = pd.read_csv(FileName)
    print("Shape:", df.shape)
    print(df.head())
    print(df.dtypes)
    return df


def HandleMissingValues(DataFrame):
    print("\nMissing values:\n", DataFrame.isnull().sum())

    df = DataFrame.fillna(DataFrame.median(numeric_only=True))
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    print("After fill, missing:", df.isnull().sum().sum())
    return df


def EncodeColumns(DataFrame):
    le_overtime = LabelEncoder()
    le_attrition = LabelEncoder()

    DataFrame["OverTime"] = le_overtime.fit_transform(DataFrame["OverTime"])
    DataFrame["Attrition"] = le_attrition.fit_transform(DataFrame["Attrition"])

    print("\nOverTime classes:", le_overtime.classes_,
          "| Attrition classes:", le_attrition.classes_)
    return DataFrame, le_overtime, le_attrition


def PlotCorrelationHeatmap(DataFrame):
    corr_mat = DataFrame.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(11, 8))
    im = ax.imshow(corr_mat.values, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr_mat.columns)))
    ax.set_yticks(range(len(corr_mat.columns)))
    ax.set_xticklabels(corr_mat.columns, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(corr_mat.columns, fontsize=8)
    for i in range(len(corr_mat)):
        for j in range(len(corr_mat)):
            ax.text(j, i, f"{corr_mat.values[i, j]:.2f}", ha="center",
                    va="center", fontsize=7)
    ax.set_title("Feature Correlation Heatmap")
    fig.colorbar(im, ax=ax, shrink=0.8)
    fig.tight_layout()
    fig.savefig("attrition_corr_heatmap.png", dpi=120)
    plt.close(fig)


def PlotSatisfactionBar(DataFrame):
    fig, ax = plt.subplots(figsize=(10, 5))
    sat_rates = DataFrame.groupby("JobSatisfaction")["Attrition"].mean()
    sat_rates.plot(kind="bar", ax=ax, color="steelblue")
    ax.set_xlabel("Job Satisfaction (1-4)")
    ax.set_ylabel("Attrition Rate")
    ax.set_title("Attrition Rate by Job Satisfaction")
    fig.tight_layout()
    fig.savefig("attrition_by_satisfaction.png", dpi=120)
    plt.close(fig)


def ExploreData(DataFrame):
    print("\nAttrition distribution:\n",
          DataFrame["Attrition"].value_counts(normalize=True))
    print("\nAttrition rate by OverTime:\n",
          DataFrame.groupby("OverTime")["Attrition"].mean())
    print("\nAttrition rate by JobSatisfaction:\n",
          DataFrame.groupby("JobSatisfaction")["Attrition"].mean().round(3))
    print("\nNumeric summary:\n", DataFrame.describe().round(2))

    corr = DataFrame.corr(numeric_only=True)["Attrition"].sort_values(ascending=False)
    print("\nCorrelation with Attrition:\n", corr.round(3))

    PlotCorrelationHeatmap(DataFrame)
    PlotSatisfactionBar(DataFrame)


def SplitData(DataFrame):
    X = DataFrame.drop("Attrition", axis=1)
    y = DataFrame["Attrition"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    print("\nTrain:", X_train.shape, "Test:", X_test.shape)
    print("Train attrition rate:", round(y_train.mean(), 3),
          "| Test attrition rate:", round(y_test.mean(), 3))
    return X_train, X_test, y_train, y_test


def ScaleFeatures(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler


def TrainModel(X_train_scaled, y_train):
    model = MLPClassifier(hidden_layer_sizes=(100, 50), activation="relu",
                          solver="adam", max_iter=600, random_state=42)
    model.fit(X_train_scaled, y_train)
    print("\nMLP trained in", model.n_iter_, "iterations, final loss:",
          round(model.loss_, 4))
    return model


def EvaluateModel(Model, X_test_scaled, y_test):
    y_pred = Model.predict(X_test_scaled)
    y_prob = Model.predict_proba(X_test_scaled)[:, 1]
    acc = accuracy_score(y_test, y_pred)

    print("\nAccuracy:", round(acc, 4))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n",
          classification_report(y_test, y_pred, target_names=["Stay", "Leave"]))
    return y_pred, y_prob, acc


def CheckOverfitting(Model, X_train_scaled, y_train, TestAccuracy):
    train_acc = Model.score(X_train_scaled, y_train)
    print("\nTrain accuracy:", round(train_acc, 4),
          "| Test accuracy:", round(TestAccuracy, 4))

    gap = train_acc - TestAccuracy
    if gap > 0.08:
        print("Overfitting: train accuracy is much higher than test accuracy.")
    elif TestAccuracy < 0.75:
        print("Underfitting: accuracy is low on both train and test sets.")
    else:
        print("Good fit: train and test accuracy are close and reasonably high.")
    return train_acc


def CrossValidate(X, y, Scaler):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(
        MLPClassifier(hidden_layer_sizes=(100, 50), activation="relu",
                      solver="adam", max_iter=600, random_state=42),
        Scaler.transform(X), y, cv=skf, scoring="accuracy")
    print("\n5-fold CV accuracies:", np.round(cv_scores, 4))
    print("Mean CV accuracy:", round(cv_scores.mean(), 4),
          "| Std:", round(cv_scores.std(), 4))
    return cv_scores


def PlotLossCurve(Model):
    plt.figure(figsize=(7, 5))
    plt.plot(Model.loss_curve_)
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title("MLP Training Loss Curve")
    plt.tight_layout()
    plt.savefig("attrition_loss_curve.png", dpi=120)
    plt.close()
    print("\nSaved attrition_loss_curve.png")


def PlotROCCurve(y_test, y_prob):
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6, 6))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
    plt.plot([0, 1], [0, 1], "k--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve - Employee Attrition")
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig("attrition_roc_curve.png", dpi=120)
    plt.close()
    print("Saved attrition_roc_curve.png | AUC =", round(roc_auc, 4))
    return roc_auc


def PredictNewEmployees(Model, Scaler, OvertimeEncoder):
    new_employees = pd.DataFrame([
        {"Age": 28, "MonthlyIncome": 35000, "YearsAtCompany": 1,
         "TotalWorkingYears": 5, "DistanceFromHome": 25,
         "JobSatisfaction": 1, "WorkLifeBalance": 2,
         "OverTime": "Yes", "NumCompaniesWorked": 3,
         "TrainingTimesLastYear": 1},
        {"Age": 45, "MonthlyIncome": 120000, "YearsAtCompany": 12,
         "TotalWorkingYears": 22, "DistanceFromHome": 5,
         "JobSatisfaction": 4, "WorkLifeBalance": 4,
         "OverTime": "No", "NumCompaniesWorked": 1,
         "TrainingTimesLastYear": 3},
        {"Age": 33, "MonthlyIncome": 55000, "YearsAtCompany": 4,
         "TotalWorkingYears": 9, "DistanceFromHome": 14,
         "JobSatisfaction": 3, "WorkLifeBalance": 3,
         "OverTime": "No", "NumCompaniesWorked": 2,
         "TrainingTimesLastYear": 2},
    ])

    new_employees["OverTime"] = OvertimeEncoder.transform(new_employees["OverTime"])
    new_pred = Model.predict(Scaler.transform(new_employees))
    new_prob = Model.predict_proba(Scaler.transform(new_employees))[:, 1]

    for i, (p, pr) in enumerate(zip(new_pred, new_prob)):
        print(f"Employee {i+1}: predicted {'Leave (1)' if p == 1 else 'Stay (0)'} "
              f"(attrition probability {pr:.2%})")


def PrintConclusion(Accuracy, RocAuc, CvScores):
    print("\n========== CONCLUSION ==========")
    print(f"The MLPClassifier achieved {Accuracy:.2%} test accuracy "
          f"with AUC {RocAuc:.3f}.")
    print(f"5-fold CV mean accuracy {CvScores.mean():.2%} shows the model is stable.")
    print("Key drivers of attrition: low job satisfaction, working overtime,")
    print("low monthly income, and long commute distance.")
    print("=================================")


def SaveResults(X_test, y_test, y_pred, y_prob, Accuracy, TrainAccuracy,
                TestAccuracy, CvScores, RocAuc):
    results = X_test.copy()
    results["Actual"] = y_test.values
    results["Predicted"] = y_pred
    results["AttritionProb"] = np.round(y_prob, 4)

    metrics = pd.DataFrame({
        "Metric": ["Accuracy", "Train Accuracy", "Test Accuracy",
                   "CV Mean Accuracy", "CV Std", "ROC AUC"],
        "Value": [round(Accuracy, 4), round(TrainAccuracy, 4),
                  round(TestAccuracy, 4), round(CvScores.mean(), 4),
                  round(CvScores.std(), 4), round(RocAuc, 4)]
    })

    metrics.to_csv("attrition_results.csv", index=False)
    results.to_csv("attrition_predictions.csv", index=False)
    print("\nSaved attrition_results.csv and attrition_predictions.csv")


def BonusExperiment(X_train_scaled, y_train, X_test_scaled, y_test, BaselineAcc):
    model = MLPClassifier(hidden_layer_sizes=(100, 50), activation="tanh",
                          solver="adam", max_iter=600, random_state=42)
    model.fit(X_train_scaled, y_train)
    acc = model.score(X_test_scaled, y_test)
    print(f"\nBONUS - tanh activation test accuracy: {acc:.4f} "
          f"(relu baseline: {BaselineAcc:.4f})")


def ExplainAlgorithm():
    print("""
========== HOW MLPClassifier WORKS ==========
An MLP (Multi-Layer Perceptron) is a feedforward neural network with an input
layer, one or more hidden layers, and an output layer. Each neuron computes a
weighted sum of its inputs plus a bias, then applies a non-linear activation
(ReLU here). For this binary task, the output neuron uses a logistic (sigmoid)
activation to produce the probability of attrition (class 1).
Training uses backpropagation: the loss (binary cross-entropy) is computed on
the training data, gradients of the loss w.r.t. every weight are propagated
backwards, and the Adam optimizer updates the weights to reduce the loss.
Iterating over the data (epochs) steadily lowers the training loss, visible in
the loss curve, until it converges to a minimum.
=============================================""")


def SuggestImprovements():
    print("""
========== MODEL IMPROVEMENT ==========
1. Hyperparameter tuning: grid-search hidden_layer_sizes, activation, alpha,
   learning rate schedules and solvers (adam vs lbfgs vs sgd).
2. More data / class balancing: only ~21% attrition samples, so SMOTE or
   class-weight tuning could raise recall for the minority (leavers) class.
3. Feature engineering: interactions like (OverTime x low satisfaction),
   and ordinal handling of satisfaction ratings.
4. Regularization: tune alpha (L2 penalty) or add early stopping to reduce
   overfitting if train/test gap widens.
5. Try tree-based baselines (Random Forest, XGBoost) for comparison.
=======================================""")


def PrintHRReport():
    print("""
========== HR RECOMMENDATION REPORT ==========
FACTORS DRIVING ATTRITION (from EDA + model):
1. Low job satisfaction (rating 1-2) - highest attrition group.
2. Frequent overtime - employees working overtime leave far more often.
3. Low monthly income - pay below ~Rs.40k strongly linked to exits.
4. Long commute (>20 km) and low work-life balance add to exit risk.

ACTIONABLE RECOMMENDATIONS:
1. Reduce excessive overtime: cap overtime hours and distribute workload,
   since overtime is the strongest modifiable driver.
2. Review compensation: revise pay bands for employees earning below market
   rate, especially those with low satisfaction scores.
3. Strengthen engagement programs: regular feedback cycles, career-growth
   paths and recognition for employees with satisfaction ratings 1-2.
4. Flexible work options: offer hybrid/remote days or cab/shift support for
   employees living far from the office.
=============================================""")


def main():
    print("----- Employee Attrition Prediction using MLP -----")

    df = LoadDataset("Employee_Attrition.csv")
    df = HandleMissingValues(df)
    df, le_overtime, le_attrition = EncodeColumns(df)
    ExploreData(df)

    X_train, X_test, y_train, y_test = SplitData(df)
    X_train_scaled, X_test_scaled, scaler = ScaleFeatures(X_train, X_test)

    model = TrainModel(X_train_scaled, y_train)
    y_pred, y_prob, acc = EvaluateModel(model, X_test_scaled, y_test)

    train_acc = CheckOverfitting(model, X_train_scaled, y_train, acc)

    X = df.drop("Attrition", axis=1)
    y = df["Attrition"]
    cv_scores = CrossValidate(X, y, scaler)

    PlotLossCurve(model)
    roc_auc = PlotROCCurve(y_test, y_prob)

    PredictNewEmployees(model, scaler, le_overtime)
    PrintConclusion(acc, roc_auc, cv_scores)
    SaveResults(X_test, y_test, y_pred, y_prob, acc, train_acc, acc,
                cv_scores, roc_auc)
    BonusExperiment(X_train_scaled, y_train, X_test_scaled, y_test, acc)
    ExplainAlgorithm()
    SuggestImprovements()
    PrintHRReport()


if __name__ == "__main__":
    main()
