"""
Question 9:
Consider the dataset below:

StudyHours | SleepHours | Marks
1          | 7          | 50
2          | 6          | 55
3          | 7          | 60
4          | 6          | 65
5          | 8          | 70

Write a Python program to:
- Train a regression model using this dataset
- Print the coefficients for both features
- Print the intercept
"""

from sklearn.linear_model import LinearRegression


def CreateDataset():
    X = [[1, 7], [2, 6], [3, 7], [4, 6], [5, 8]]
    marks = [50, 55, 60, 65, 70]
    return X, marks


def TrainModel(X, Y):
    model = LinearRegression()
    model.fit(X, Y)
    return model


def DisplayResults(Model):
    print("Coefficient (StudyHours):", Model.coef_[0])
    print("Coefficient (SleepHours):", Model.coef_[1])
    print("Intercept:", Model.intercept_)


def main():
    print("----- Linear Regression : Two Features -----")

    X, marks = CreateDataset()
    model = TrainModel(X, marks)
    DisplayResults(model)


if __name__ == "__main__":
    main()
