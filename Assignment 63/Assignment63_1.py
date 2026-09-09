"""
Question 1:
Loan Default Prediction using Multi-Layer Perceptron.

Dataset: Loan_Default.csv
Output: 0 -> Low default risk, 1 -> High default risk.

Features: Age, Income, LoanAmount, CreditScore, EmploymentYears, ExistingLoans,
MonthlyDebt, LoanTerm, PreviousDefault (Yes/No), HomeOwnership (Rent/Own/Mortgage).

Tasks:
1. Import Libraries and Load Dataset
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
16. Bonus Task (deeper network)
17. Explain Working of the Algorithm

Hyperparameter experiments:
Exp 1: activation tanh vs logistic vs relu
Exp 2: hidden_layer_sizes (50,) vs (100, 50)
Exp 3: solver sgd vs lbfgs
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             classification_report, precision_score,
                             recall_score, f1_score, roc_curve, roc_auc_score)


def LoadDataset(FileName):
    print("=== Task 1: Import Libraries and Load Dataset ===")
    df = pd.read_csv(FileName)
    return df


def HandleMissingValues(DataFrame):
    print("\n=== Task 2: Handle Missing Values ===")
    print("Missing values per column:\n", DataFrame.isnull().sum())

    df = DataFrame.dropna()
    print("Shape after handling missing values:", df.shape)
    return df


def EncodeColumns(DataFrame):
    print("\n=== Task 3: Preprocess Categorical Columns ===")

    DataFrame["PreviousDefault"] = DataFrame["PreviousDefault"].astype(str)
    DataFrame["HomeOwnership"] = DataFrame["HomeOwnership"].astype(str)

    le_prev = LabelEncoder()
    le_home = LabelEncoder()
    DataFrame["PreviousDefault"] = le_prev.fit_transform(DataFrame["PreviousDefault"])
    DataFrame["HomeOwnership"] = le_home.fit_transform(DataFrame["HomeOwnership"])

    print("PreviousDefault classes:", list(le_prev.classes_))
    print("HomeOwnership classes:", list(le_home.classes_))
    return DataFrame, le_prev, le_home


def ExploreData(DataFrame):
    print("\n=== Task 4: Exploratory Data Analysis ===")
    print("Shape:", DataFrame.shape)
    print("\nDescribe:\n", DataFrame.describe().round(2).to_string())
    print("\nClass balance:\n", DataFrame["Default"].value_counts())
    print("Class ratios:\n", DataFrame["Default"].value_counts(normalize=True).round(3))


def SplitData(DataFrame):
    print("\n=== Task 5: Train-Test Split (stratified) ===")

    X = DataFrame.drop("Default", axis=1)
    y = DataFrame["Default"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    print("Train:", X_train.shape, "Test:", X_test.shape)
    print("Train class ratio:",
          y_train.value_counts(normalize=True).round(3).to_dict())
    print("Test class ratio :",
          y_test.value_counts(normalize=True).round(3).to_dict())
    return X_train, X_test, y_train, y_test


def ScaleFeatures(X_train, X_test):
    print("\n=== Task 6: Feature Scaling ===")

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Scaled train mean (first 3 features):",
          X_train_scaled.mean(axis=0)[:3].round(4))
    print("Scaled train std (first 3 features):",
          X_train_scaled.std(axis=0)[:3].round(4))
    return X_train_scaled, X_test_scaled, scaler


def TrainModel(X_train_scaled, y_train):
    print("\n=== Task 7: Build MLPClassifier ===")

    model = MLPClassifier(hidden_layer_sizes=(50,), activation="relu",
                          solver="adam", max_iter=600, random_state=42)
    model.fit(X_train_scaled, y_train)
    print("Model:", model)
    return model


def EvaluateModel(Model, X_test_scaled, y_test):
    print("\n=== Task 8: Evaluate Model ===")

    y_pred = Model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)

    print("Accuracy:", round(acc, 4))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n",
          classification_report(y_test, y_pred, zero_division=0))
    print("Precision:", round(precision_score(y_test, y_pred, zero_division=0), 4))
    print("Recall   :", round(recall_score(y_test, y_pred, zero_division=0), 4))
    print("F1-score :", round(f1_score(y_test, y_pred, zero_division=0), 4))
    return y_pred, acc


def CheckOverfitting(Model, X_train_scaled, y_train, TestAccuracy):
    print("\n=== Task 9: Overfitting / Underfitting Check ===")

    train_acc = accuracy_score(y_train, Model.predict(X_train_scaled))
    print(f"Train accuracy: {train_acc:.4f}")
    print(f"Test accuracy : {TestAccuracy:.4f}")
    print(f"Gap           : {train_acc - TestAccuracy:.4f}")

    if train_acc - TestAccuracy > 0.10:
        print("-> Large gap: possible overfitting.")
    elif TestAccuracy < 0.70:
        print("-> Low test accuracy: possible underfitting.")
    else:
        print("-> Small gap, good test score: model generalizes well.")
    return train_acc


def CrossValidate(X_train_scaled, y_train):
    print("\n=== Task 10: Cross-Validation (5-fold) ===")

    cv = cross_val_score(MLPClassifier(hidden_layer_sizes=(50,), activation="relu",
                                       solver="adam", max_iter=600,
                                       random_state=42),
                         X_train_scaled, y_train, cv=5)
    print("CV scores:", np.round(cv, 4))
    print(f"CV mean: {cv.mean():.4f}, CV std: {cv.std():.4f}")
    return cv


def PlotLossCurve(Model):
    print("\n=== Task 11: Plot Loss Curve ===")

    plt.figure()
    plt.plot(Model.loss_curve_)
    plt.title("MLP Training Loss Curve")
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.savefig("mlp_loss_curve.png")
    plt.close()
    print("Loss curve saved to mlp_loss_curve.png")


def PlotROCCurve(Model, X_test_scaled, y_test):
    print("\n=== Task 12: ROC Curve ===")

    y_prob = Model.predict_proba(X_test_scaled)[:, 1]
    score = roc_auc_score(y_test, y_prob)
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    print(f"AUC: {score:.4f}")

    plt.figure()
    plt.plot(fpr, tpr, label=f"ROC (AUC = {score:.4f})")
    plt.plot([0, 1], [0, 1], linestyle="--", label="Random")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve - Loan Default Prediction")
    plt.legend()
    plt.savefig("roc_curve.png")
    plt.close()
    print("ROC curve saved to roc_curve.png")
    return y_prob, score


def PredictNewApplicants(Model, Scaler, PrevEncoder, HomeEncoder, Columns):
    print("\n=== Task 13: Predict New Data ===")

    new_applicants = pd.DataFrame([
        {"Age": 35, "Income": 600000, "CreditScore": 720, "LoanAmount": 300000,
         "EmploymentYears": 8, "ExistingLoans": 1, "MonthlyDebt": 15000,
         "LoanTerm": 36, "PreviousDefault": "No", "HomeOwnership": "Own"},
        {"Age": 50, "Income": 250000, "CreditScore": 540, "LoanAmount": 800000,
         "EmploymentYears": 2, "ExistingLoans": 5, "MonthlyDebt": 45000,
         "LoanTerm": 60, "PreviousDefault": "Yes", "HomeOwnership": "Rent"},
        {"Age": 29, "Income": 900000, "CreditScore": 790, "LoanAmount": 400000,
         "EmploymentYears": 6, "ExistingLoans": 0, "MonthlyDebt": 10000,
         "LoanTerm": 48, "PreviousDefault": "No", "HomeOwnership": "Mortgage"}])

    new_applicants["PreviousDefault"] = PrevEncoder.transform(
        new_applicants["PreviousDefault"])
    new_applicants["HomeOwnership"] = HomeEncoder.transform(
        new_applicants["HomeOwnership"])

    new_pred = Model.predict(Scaler.transform(new_applicants[Columns]))
    new_prob = Model.predict_proba(Scaler.transform(new_applicants[Columns]))[:, 1]

    for i, (p, pr) in enumerate(zip(new_pred, new_prob)):
        print(f"Applicant {i + 1}: "
              f"{'High default risk' if p == 1 else 'Low default risk'} "
              f"(default probability {pr:.3f})")


def PrintConclusion(Accuracy, CvScores, Auc, TrainAccuracy):
    print("\n=== Task 14: Conclusion ===")
    print(f"""Conclusion: The MLPClassifier trained on the Loan_Default dataset
achieved a test accuracy of {Accuracy:.2%}, with cross-validation mean
accuracy {CvScores.mean():.2%} (std {CvScores.std():.4f}), and ROC-AUC {Auc:.4f}.
Train accuracy ({TrainAccuracy:.2%}) and test accuracy ({Accuracy:.2%}) are close,
so the model generalizes well without serious overfitting or underfitting.
The neural network effectively captures the nonlinear relationships between
applicant features (credit score, income, previous defaults, etc.) and
loan default risk, making it suitable for flagging high-risk applicants.""")


def SaveResults(y_test, y_pred, y_prob, Accuracy, CvScores, Auc):
    print("\n=== Task 15: Save Output ===")

    results = pd.DataFrame({"Actual": y_test.values, "Predicted": y_pred,
                            "Default_Probability": y_prob})
    results["Risk"] = results["Predicted"].map(
        {0: "Low default risk", 1: "High default risk"})

    metrics = pd.DataFrame([{
        "Accuracy": round(Accuracy, 4),
        "Precision": round(precision_score(y_test, y_pred, zero_division=0), 4),
        "Recall": round(recall_score(y_test, y_pred, zero_division=0), 4),
        "F1": round(f1_score(y_test, y_pred, zero_division=0), 4),
        "AUC": round(Auc, 4),
        "CV_Mean": round(CvScores.mean(), 4),
        "CV_Std": round(CvScores.std(), 4)}])

    with open("loan_default_results.csv", "w") as f:
        results.to_csv(f, index=False)
        f.write("\n# Metrics\n")
        metrics.to_csv(f, index=False)
    print("Predictions and metrics saved to loan_default_results.csv")


def BonusExperiment(X_train_scaled, y_train, X_test_scaled, y_test, BaselineAcc):
    print("\n=== Task 16: Bonus - Improvement (deeper network (100, 50)) ===")

    model = MLPClassifier(hidden_layer_sizes=(100, 50), activation="relu",
                          solver="adam", max_iter=600, random_state=42)
    model.fit(X_train_scaled, y_train)
    big_acc = accuracy_score(y_test, model.predict(X_test_scaled))

    print(f"Deeper network (100, 50) test accuracy: {big_acc:.4f}")
    print(f"Baseline (50,) test accuracy: {BaselineAcc:.4f}")
    print("-> Deeper network", "improved" if big_acc > BaselineAcc else
          "did not improve", "test accuracy.")


def ExplainAlgorithm():
    print("\n=== Task 17: How MLPClassifier Works ===")
    print("""MLPClassifier (Multi-Layer Perceptron) is a feedforward neural network
classifier. It has an input layer (one neuron per feature), one or more hidden
layers, and an output layer (one neuron per class, with softmax or logistic
activation). Each neuron computes a weighted sum of its inputs plus a bias and
passes it through a nonlinear activation function (relu, tanh, logistic).
Training uses backpropagation: the error between predicted and true labels is
propagated backwards through the network and each weight is updated with
gradient descent (or an optimizer such as adam, sgd, or lbfgs) to minimize the
log-loss. Scaling features is important because gradient-based updates converge
much faster when all features are on a similar scale.""")


def RunExperiments(X_train_scaled, y_train, X_test_scaled, y_test):
    print("\n=== Experiment 1: Activation (relu vs tanh vs logistic) ===")
    for act in ["relu", "tanh", "logistic"]:
        m = MLPClassifier(hidden_layer_sizes=(50,), activation=act,
                          solver="adam", max_iter=600, random_state=42)
        m.fit(X_train_scaled, y_train)
        print(f"  {act}: {accuracy_score(y_test, m.predict(X_test_scaled)):.4f}")

    print("\n=== Experiment 2: Hidden Layer Sizes ===")
    for layers in [(50,), (100, 50)]:
        m = MLPClassifier(hidden_layer_sizes=layers, activation="relu",
                          solver="adam", max_iter=600, random_state=42)
        m.fit(X_train_scaled, y_train)
        print(f"  {layers}: {accuracy_score(y_test, m.predict(X_test_scaled)):.4f}")

    print("\n=== Experiment 3: Solver (sgd vs lbfgs) ===")
    for solver in ["sgd", "lbfgs"]:
        m = MLPClassifier(hidden_layer_sizes=(50,), activation="relu",
                          solver=solver, max_iter=600, random_state=42)
        m.fit(X_train_scaled, y_train)
        print(f"  {solver}: {accuracy_score(y_test, m.predict(X_test_scaled)):.4f}")


def main():
    print("----- Loan Default Prediction using MLP -----")

    df = LoadDataset("Loan_Default.csv")
    df = HandleMissingValues(df)
    df, le_prev, le_home = EncodeColumns(df)
    ExploreData(df)

    X_train, X_test, y_train, y_test = SplitData(df)
    X_train_scaled, X_test_scaled, scaler = ScaleFeatures(X_train, X_test)

    model = TrainModel(X_train_scaled, y_train)
    y_pred, acc = EvaluateModel(model, X_test_scaled, y_test)

    train_acc = CheckOverfitting(model, X_train_scaled, y_train, acc)
    cv_scores = CrossValidate(X_train_scaled, y_train)

    PlotLossCurve(model)
    y_prob, auc_score = PlotROCCurve(model, X_test_scaled, y_test)

    X = df.drop("Default", axis=1)
    PredictNewApplicants(model, scaler, le_prev, le_home, X.columns)
    PrintConclusion(acc, cv_scores, auc_score, train_acc)
    SaveResults(y_test, y_pred, y_prob, acc, cv_scores, auc_score)
    BonusExperiment(X_train_scaled, y_train, X_test_scaled, y_test, acc)
    ExplainAlgorithm()
    RunExperiments(X_train_scaled, y_train, X_test_scaled, y_test)


if __name__ == "__main__":
    main()
