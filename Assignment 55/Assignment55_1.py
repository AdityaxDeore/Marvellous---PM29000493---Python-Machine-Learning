"""
Question 1:
Customer Loan Approval Using Voting Classification.

A bank wants to automate its loan approval process.
Features: Income, Credit Score, Existing Loan, Employment Experience, Loan Amount.
Target: LoanApproved (0 -> Loan Rejected, 1 -> Loan Approved).

The bank does not want to depend on a single Machine Learning algorithm.
Build a Voting Classifier using Logistic Regression, Decision Tree and KNN.

Tasks:
1. Load the dataset.
2. Check for missing values.
3. Separate input and output variables.
4. Split the dataset into training and testing data.
5. Train Logistic Regression.
6. Train Decision Tree.
7. Train KNN.
8. Calculate the individual accuracy of all three algorithms.
9. Create a Hard Voting Classifier.
10. Calculate its accuracy.
11. Create a Soft Voting Classifier.
12. Calculate its accuracy.
13. Compare the models.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


def LoadDataset(FileName):
    df = pd.read_csv(FileName)
    print("Shape:", df.shape)
    print(df.head().to_string())
    return df


def CheckMissingValues(DataFrame):
    print("\nMissing values:\n", DataFrame.isnull().sum())


def SplitData(DataFrame, TargetColumn):
    X = DataFrame.drop(TargetColumn, axis=1)
    y = DataFrame[TargetColumn]
    print("\nFeatures:", list(X.columns))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y)
    print(f"Train: {X_train.shape}, Test: {X_test.shape}")
    return X_train, X_test, y_train, y_test


def TrainModels(X_train, y_train):
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)

    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, y_train)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    return lr, dt, knn


def EvaluateModel(Model, X_test, y_test):
    return accuracy_score(y_test, Model.predict(X_test))


def BuildVotingClassifier(Estimators, X_train, y_train, VotingType):
    voting = VotingClassifier(estimators=Estimators, voting=VotingType)
    voting.fit(X_train, y_train)
    return voting


def DisplayComparison(Results):
    print("\nComparison:")
    print(pd.DataFrame(Results).to_string(index=False))


def main():
    print("----- Customer Loan Approval using Voting Classification -----")

    df = LoadDataset("Customer_Loan_Approval.csv")
    CheckMissingValues(df)
    X_train, X_test, y_train, y_test = SplitData(df, "LoanApproved")

    lr, dt, knn = TrainModels(X_train, y_train)

    acc_lr = EvaluateModel(lr, X_test, y_test)
    acc_dt = EvaluateModel(dt, X_test, y_test)
    acc_knn = EvaluateModel(knn, X_test, y_test)
    print(f"\nLogistic Regression accuracy: {acc_lr:.4f}")
    print(f"Decision Tree accuracy:       {acc_dt:.4f}")
    print(f"KNN accuracy:                 {acc_knn:.4f}")

    estimators = [("lr", lr), ("dt", dt), ("knn", knn)]

    hard_vote = BuildVotingClassifier(estimators, X_train, y_train, "hard")
    acc_hard = EvaluateModel(hard_vote, X_test, y_test)
    print(f"Hard Voting accuracy:         {acc_hard:.4f}")

    soft_vote = BuildVotingClassifier(estimators, X_train, y_train, "soft")
    acc_soft = EvaluateModel(soft_vote, X_test, y_test)
    print(f"Soft Voting accuracy:         {acc_soft:.4f}")

    results = {"Model": ["Logistic Regression", "Decision Tree", "KNN",
                         "Hard Voting", "Soft Voting"],
               "Accuracy": [acc_lr, acc_dt, acc_knn, acc_hard, acc_soft]}
    DisplayComparison(results)

    best_model = max(results["Model"],
                     key=lambda m: results["Accuracy"][results["Model"].index(m)])
    print(f"\nConclusion: {best_model} performed best with accuracy "
          f"{max(results['Accuracy']):.4f}.")


if __name__ == "__main__":
    main()
