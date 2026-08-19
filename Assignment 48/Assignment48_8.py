"""
Question 8:
Create a program that:
a) Trains KNN models with K = 1, 3, 5, and 7 on the same dataset.
b) Predicts the class for a test point using each model.
c) Prints the predicted class for each value of K.
"""

from sklearn.neighbors import KNeighborsClassifier


def CreateDataset():
    x_train = [[2, 3], [3, 4], [4, 3], [2, 4], [3, 3], [4, 4], [1, 2],
               [5, 3], [3, 2], [2, 5],
               [7, 8], [8, 7], [6, 9], [7, 7], [8, 8], [6, 8], [9, 7],
               [7, 9], [9, 8], [6, 7]]
    y_train = ['A'] * 10 + ['B'] * 10
    return x_train, y_train


def PredictWithK(XTrain, YTrain, TestPoint, K):
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(XTrain, YTrain)
    return model.predict(TestPoint)[0]


def main():
    print("----- KNN Prediction for Different K Values -----")

    x_train, y_train = CreateDataset()
    test_point = [[5, 5]]

    for k in [1, 3, 5, 7]:
        predicted = PredictWithK(x_train, y_train, test_point, k)
        print(f"K = {k}: predicted class =", predicted)


if __name__ == "__main__":
    main()
