"""
Question 9:
Write a Python program to:
a) Split a dataset into training and testing sets using train_test_split.
b) Train KNN models with K values from 1 to 10.
c) Calculate the accuracy for each K and print the K with the highest accuracy.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def LoadAndSplit():
    X, y = load_iris(return_X_y=True)
    return train_test_split(X, y, test_size=0.3, random_state=42)


def CalculateAccuracy(XTrain, XTest, YTrain, YTest, K):
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(XTrain, YTrain)
    return accuracy_score(YTest, model.predict(XTest))


def main():
    print("----- Find Best K for KNN -----")

    x_train, x_test, y_train, y_test = LoadAndSplit()

    best_k = 1
    best_accuracy = 0.0

    for k in range(1, 11):
        accuracy = CalculateAccuracy(x_train, x_test, y_train, y_test, k)
        print(f"K = {k}: accuracy = {accuracy:.4f}")
        if accuracy > best_accuracy:
            best_k = k
            best_accuracy = accuracy

    print("Best K:", best_k, "with accuracy:", round(best_accuracy, 4))


if __name__ == "__main__":
    main()
