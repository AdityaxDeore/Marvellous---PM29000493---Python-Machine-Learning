import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")
X = df.drop("Fraud", axis=1)
y = df["Fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

model = VotingClassifier(estimators=[
    ("lr", make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))),
    ("dt", DecisionTreeClassifier(random_state=42)),
    ("knn", make_pipeline(StandardScaler(), KNeighborsClassifier()))
], voting="hard")
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Voting Classifier (Logistic Regression + Decision Tree + KNN, hard voting)")
print("Accuracy :", round(accuracy_score(y_test, y_pred), 4))
print("Precision:", round(precision_score(y_test, y_pred, zero_division=0), 4))
print("Recall   :", round(recall_score(y_test, y_pred, zero_division=0), 4))
print("F1 Score :", round(f1_score(y_test, y_pred, zero_division=0), 4))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
