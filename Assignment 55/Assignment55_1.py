"""
Marvellous Infosystems - Machine Learning Assignment 55
Customer Loan Approval using Voting Classification
Dataset: Customer_Loan_Approval.csv | Target: LoanApproved (0=rejected, 1=approved)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


def main():
    # 1. Load dataset
    df = pd.read_csv("Customer_Loan_Approval.csv")
    print("Shape:", df.shape)
    print(df.head().to_string())

    # 2. Check missing values
    print("\nMissing values:\n", df.isnull().sum())

    # 3. Separate features X and target y
    X = df.drop("LoanApproved", axis=1)
    y = df["LoanApproved"]
    print("\nFeatures:", list(X.columns))

    # 4. Train-test split (stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y)
    print(f"Train: {X_train.shape}, Test: {X_test.shape}")

    # 5. Train Logistic Regression
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)

    # 6. Train Decision Tree
    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, y_train)

    # 7. Train KNN
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    # 8. Individual accuracies
    acc_lr = accuracy_score(y_test, lr.predict(X_test))
    acc_dt = accuracy_score(y_test, dt.predict(X_test))
    acc_knn = accuracy_score(y_test, knn.predict(X_test))
    print(f"\nLogistic Regression accuracy: {acc_lr:.4f}")
    print(f"Decision Tree accuracy:       {acc_dt:.4f}")
    print(f"KNN accuracy:                 {acc_knn:.4f}")

    # 9. Hard Voting Classifier
    hard_vote = VotingClassifier(
        estimators=[("lr", lr), ("dt", dt), ("knn", knn)],
        voting="hard")
    hard_vote.fit(X_train, y_train)

    # 10. Hard voting accuracy
    acc_hard = accuracy_score(y_test, hard_vote.predict(X_test))
    print(f"Hard Voting accuracy:         {acc_hard:.4f}")

    # 11. Soft Voting Classifier
    soft_vote = VotingClassifier(
        estimators=[("lr", lr), ("dt", dt), ("knn", knn)],
        voting="soft")
    soft_vote.fit(X_train, y_train)

    # 12. Soft voting accuracy
    acc_soft = accuracy_score(y_test, soft_vote.predict(X_test))
    print(f"Soft Voting accuracy:         {acc_soft:.4f}")

    # 13. Comparison table + conclusion
    results = {"Model": ["Logistic Regression", "Decision Tree", "KNN",
                         "Hard Voting", "Soft Voting"],
               "Accuracy": [acc_lr, acc_dt, acc_knn, acc_hard, acc_soft]}
    print("\nComparison:")
    print(pd.DataFrame(results).to_string(index=False))
    best = max(results["Model"], key=lambda m: results["Accuracy"][results["Model"].index(m)])
    print(f"\nConclusion: {best} performed best with accuracy "
          f"{max(results['Accuracy']):.4f}.")


if __name__ == "__main__":
    main()
