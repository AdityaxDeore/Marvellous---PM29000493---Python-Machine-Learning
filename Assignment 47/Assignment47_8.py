"""
Question 8:
Using the regression model created in the previous question, write a Python
program to predict marks for 6 study hours and display the predicted value.

Expected Output: Predicted marks for 6 study hours: 75.0
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


def PredictMarks(Model, Hours):
    return Model.predict([[Hours]])[0]


def main():
    print("----- Linear Regression : Predict Marks -----")

    study_hours, marks = CreateDataset()
    model = TrainModel(study_hours, marks)

    predicted = PredictMarks(model, 6)
    print("Predicted marks for 6 study hours:", predicted)


if __name__ == "__main__":
    main()
