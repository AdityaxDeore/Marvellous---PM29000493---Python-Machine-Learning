"""
Question 7:
Write a Python program using KNeighborsClassifier from sklearn to:
a) Train a KNN model with K = 5.
b) Use the training data:
   X_train = [[2,3],[3,4],[4,3],[7,8],[8,7],[6,9]]
   y_train = ['A','A','A','B','B','B']
c) Predict the class for the test point [[5,5]] and print the result.
"""

from sklearn.neighbors import KNeighborsClassifier


def TrainModel(XTrain, YTrain, K):
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(XTrain, YTrain)
    return model


def main():
    print("----- KNN Classification -----")

    x_train = [[2, 3], [3, 4], [4, 3], [7, 8], [8, 7], [6, 9]]
    y_train = ['A', 'A', 'A', 'B', 'B', 'B']

    model = TrainModel(x_train, y_train, 5)
    predicted = model.predict([[5, 5]])[0]
    print("Predicted class for [5,5]:", predicted)


if __name__ == "__main__":
    main()
