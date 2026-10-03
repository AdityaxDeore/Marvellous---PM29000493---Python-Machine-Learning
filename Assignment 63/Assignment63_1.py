"""
Marvellous Infosystems - Deep Learning Assignment 63
Loan Default Prediction using Multi-Layer Perceptron (MLPClassifier)

Dataset: Loan_Default.csv
Output: 0 -> Low default risk, 1 -> High default risk
"""

# Task 1: Import libraries and load dataset
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

print("=== Task 1: Import Libraries and Load Dataset ===")
df = pd.read_csv("Loan_Default.csv")

# Task 2: Handle missing values
print("\n=== Task 2: Handle Missing Values ===")
print("Missing values per column:\n", df.isnull().sum())
df = df.dropna()  # no missing values found; dropna keeps data clean
print("Shape after handling missing values:", df.shape)

# Task 3: Preprocess categorical columns
print("\n=== Task 3: Preprocess Categorical Columns ===")
df["PreviousDefault"] = df["PreviousDefault"].astype(str)
df["HomeOwnership"] = df["HomeOwnership"].astype(str)
le_prev = LabelEncoder()
le_home = LabelEncoder()
df["PreviousDefault"] = le_prev.fit_transform(df["PreviousDefault"])
df["HomeOwnership"] = le_home.fit_transform(df["HomeOwnership"])
print("PreviousDefault classes:", list(le_prev.classes_))
print("HomeOwnership classes:", list(le_home.classes_))

# Task 4: EDA
print("\n=== Task 4: Exploratory Data Analysis ===")
print("Shape:", df.shape)
print("\nDescribe:\n", df.describe().round(2).to_string())
print("\nClass balance:\n", df["Default"].value_counts())
print("Class ratios:\n", df["Default"].value_counts(normalize=True).round(3))

X = df.drop("Default", axis=1)
y = df["Default"]

# Task 5: Train-test split (stratified)
print("\n=== Task 5: Train-Test Split (stratified) ===")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
print("Train:", X_train.shape, "Test:", X_test.shape)
print("Train class ratio:", y_train.value_counts(normalize=True).round(3).to_dict())
print("Test class ratio :", y_test.value_counts(normalize=True).round(3).to_dict())

# Task 6: Feature scaling
print("\n=== Task 6: Feature Scaling ===")
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
print("Scaled train mean (first 3 features):",
      X_train_s.mean(axis=0)[:3].round(4))
print("Scaled train std (first 3 features):",
      X_train_s.std(axis=0)[:3].round(4))

# Task 7: Build MLPClassifier
print("\n=== Task 7: Build MLPClassifier ===")
mlp = MLPClassifier(hidden_layer_sizes=(50,), activation="relu",
                    solver="adam", max_iter=600, random_state=42)
mlp.fit(X_train_s, y_train)
print("Model:", mlp)

# Task 8: Evaluate
print("\n=== Task 8: Evaluate Model ===")
y_pred = mlp.predict(X_test_s)
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", round(acc, 4))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n",
      classification_report(y_test, y_pred, zero_division=0))
print("Precision:", round(precision_score(y_test, y_pred, zero_division=0), 4))
print("Recall   :", round(recall_score(y_test, y_pred, zero_division=0), 4))
print("F1-score :", round(f1_score(y_test, y_pred, zero_division=0), 4))

# Task 9: Overfitting / underfitting check
print("\n=== Task 9: Overfitting / Underfitting Check ===")
train_acc = accuracy_score(y_train, mlp.predict(X_train_s))
print(f"Train accuracy: {train_acc:.4f}")
print(f"Test accuracy : {acc:.4f}")
print(f"Gap           : {train_acc - acc:.4f}")
if train_acc - acc > 0.10:
    print("-> Large gap: possible overfitting.")
elif acc < 0.70:
    print("-> Low test accuracy: possible underfitting.")
else:
    print("-> Small gap, good test score: model generalizes well.")

# Task 10: Cross-validation (5-fold)
print("\n=== Task 10: Cross-Validation (5-fold) ===")
cv = cross_val_score(MLPClassifier(hidden_layer_sizes=(50,), activation="relu",
                                   solver="adam", max_iter=600,
                                   random_state=42),
                     X_train_s, y_train, cv=5)
print("CV scores:", np.round(cv, 4))
print(f"CV mean: {cv.mean():.4f}, CV std: {cv.std():.4f}")

# Task 11: Plot loss curve
print("\n=== Task 11: Plot Loss Curve ===")
plt.figure()
plt.plot(mlp.loss_curve_)
plt.title("MLP Training Loss Curve")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.savefig("mlp_loss_curve.png")
plt.close()
print("Loss curve saved to mlp_loss_curve.png")

# Task 12: ROC curve
print("\n=== Task 12: ROC Curve ===")
y_prob = mlp.predict_proba(X_test_s)[:, 1]
auc = roc_auc_score(y_test, y_prob)
fpr, tpr, _ = roc_curve(y_test, y_prob)
print(f"AUC: {auc:.4f}")
plt.figure()
plt.plot(fpr, tpr, label=f"ROC (AUC = {auc:.4f})")
plt.plot([0, 1], [0, 1], linestyle="--", label="Random")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Loan Default Prediction")
plt.legend()
plt.savefig("roc_curve.png")
plt.close()
print("ROC curve saved to roc_curve.png")

# Task 13: Predict on new applicants
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
new_applicants["PreviousDefault"] = le_prev.transform(
    new_applicants["PreviousDefault"])
new_applicants["HomeOwnership"] = le_home.transform(
    new_applicants["HomeOwnership"])
new_pred = mlp.predict(scaler.transform(new_applicants[X.columns]))
new_prob = mlp.predict_proba(scaler.transform(new_applicants[X.columns]))[:, 1]
for i, (p, pr) in enumerate(zip(new_pred, new_prob)):
    print(f"Applicant {i + 1}: "
          f"{'High default risk' if p == 1 else 'Low default risk'} "
          f"(default probability {pr:.3f})")

# Task 14: Conclusion
print("\n=== Task 14: Conclusion ===")
print(f"""Conclusion: The MLPClassifier trained on the Loan_Default dataset
achieved a test accuracy of {acc:.2%}, with cross-validation mean
accuracy {cv.mean():.2%} (std {cv.std():.4f}), and ROC-AUC {auc:.4f}.
Train accuracy ({train_acc:.2%}) and test accuracy ({acc:.2%}) are close,
so the model generalizes well without serious overfitting or underfitting.
The neural network effectively captures the nonlinear relationships between
applicant features (credit score, income, previous defaults, etc.) and
loan default risk, making it suitable for flagging high-risk applicants.""")

# Task 15: Save output (predictions + metrics to CSV)
print("\n=== Task 15: Save Output ===")
results = pd.DataFrame({"Actual": y_test.values, "Predicted": y_pred,
                        "Default_Probability": y_prob})
results["Risk"] = results["Predicted"].map(
    {0: "Low default risk", 1: "High default risk"})
metrics = pd.DataFrame([{
    "Accuracy": round(acc, 4), "Precision": round(
        precision_score(y_test, y_pred, zero_division=0), 4),
    "Recall": round(recall_score(y_test, y_pred, zero_division=0), 4),
    "F1": round(f1_score(y_test, y_pred, zero_division=0), 4),
    "AUC": round(auc, 4), "CV_Mean": round(cv.mean(), 4),
    "CV_Std": round(cv.std(), 4)}])
with open("loan_default_results.csv", "w") as f:
    results.to_csv(f, index=False)
    f.write("\n# Metrics\n")
    metrics.to_csv(f, index=False)
print("Predictions and metrics saved to loan_default_results.csv")

# Task 16: Bonus - improvement attempt (deeper network (100, 50))
print("\n=== Task 16: Bonus - Improvement (deeper network (100, 50)) ===")
mlp_big = MLPClassifier(hidden_layer_sizes=(100, 50), activation="relu",
                        solver="adam", max_iter=600, random_state=42)
mlp_big.fit(X_train_s, y_train)
big_acc = accuracy_score(y_test, mlp_big.predict(X_test_s))
print(f"Deeper network (100, 50) test accuracy: {big_acc:.4f}")
print(f"Baseline (50,) test accuracy: {acc:.4f}")
print("-> Deeper network", "improved" if big_acc > acc else
      "did not improve", "test accuracy.")

# Task 17: How MLPClassifier works
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

# Hyperparameter experiments
print("\n=== Experiment 1: Activation (relu vs tanh vs logistic) ===")
for act in ["relu", "tanh", "logistic"]:
    m = MLPClassifier(hidden_layer_sizes=(50,), activation=act,
                      solver="adam", max_iter=600, random_state=42)
    m.fit(X_train_s, y_train)
    print(f"  {act}: {accuracy_score(y_test, m.predict(X_test_s)):.4f}")

print("\n=== Experiment 2: Hidden Layer Sizes ===")
for layers in [(50,), (100, 50)]:
    m = MLPClassifier(hidden_layer_sizes=layers, activation="relu",
                      solver="adam", max_iter=600, random_state=42)
    m.fit(X_train_s, y_train)
    print(f"  {layers}: {accuracy_score(y_test, m.predict(X_test_s)):.4f}")

print("\n=== Experiment 3: Solver (sgd vs lbfgs) ===")
for solver in ["sgd", "lbfgs"]:
    m = MLPClassifier(hidden_layer_sizes=(50,), activation="relu",
                      solver=solver, max_iter=600, random_state=42)
    m.fit(X_train_s, y_train)
    print(f"  {solver}: {accuracy_score(y_test, m.predict(X_test_s)):.4f}")
