"""
Question 7:
Write a Python program using LinearRegression to train a regression model
using the dataset below.

Study Hours | Marks
1           | 50
2           | 55
3           | 60
4           | 65
5           | 70

Your program should:
- Train the regression model
- Print the coefficient
- Print the intercept
"""

from sklearn.linear_model import LinearRegression


def CreateDataset():
    study_hours = [[1], [2], [3], [4], [5]]
    marks = [50, 55, 60, 65, 70]
    return study_hours, marks


def TrainModel(X, Y):
    model = LinearRegression()
    model.fit(X, Y)
    return model


def DisplayResults(Model):
    print("Coefficient:", Model.coef_[0])
    print("Intercept:", Model.intercept_)


def main():
    print("----- Linear Regression : Study Hours vs Marks -----")

    study_hours, marks = CreateDataset()
    model = TrainModel(study_hours, marks)
    DisplayResults(model)


if __name__ == "__main__":
    main()
