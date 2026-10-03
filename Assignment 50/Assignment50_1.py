import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, f1_score, precision_score,
                             recall_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load and explore the dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")
print("Shape:", X.shape)
print("Target names:", data.target_names, "(0 = Malignant, 1 = Benign)")
print("Class balance:\n", y.value_counts())

# 2. Preprocessing
print("Missing values:", X.isna().sum().sum())
scaler = StandardScaler()
Xs = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# 3. EDA
print(X.describe().T[["mean", "std", "min", "max"]])
corr_target = X.corrwith(y).abs().sort_values(ascending=False)
top = corr_target.head(10).index
print("Top 10 features by |correlation| with target:\n", corr_target.head(10))

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
y.value_counts().plot(kind="bar")
plt.xticks([0, 1], ["Malignant", "Benign"], rotation=0)
plt.title("Class distribution")
plt.tight_layout()
plt.savefig("breast_cancer_classes.png")
plt.close()

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    Xs, y, test_size=0.2, random_state=42, stratify=y)

# 5. Build model: RandomForestClassifier - robust default for tabular medical
# data, captures non-linear feature interactions, resistant to overfitting.
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")
print("Confusion Matrix:\n", cm)
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# 7. Observations and conclusions
print("Observations: worst concave points, worst perimeter and mean concave")
print("points correlate most strongly with malignancy. The Random Forest")
print("model separates benign from malignant tumors with high accuracy,")
print(f"achieving {acc:.2%} test accuracy, supporting its use as an")
print("early-detection aid alongside clinical diagnosis.")
print("Saved: breast_cancer_corr.png, breast_cancer_classes.png")
