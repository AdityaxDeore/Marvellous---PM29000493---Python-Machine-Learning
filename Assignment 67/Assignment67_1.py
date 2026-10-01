"""
Question 1:
Build a neural network to predict customer churn.

Features: Age, Monthly Charges, Tenure, Number of Complaints, Customer Support Calls.
Output: 0 -> Customer will stay, 1 -> Customer may leave.

Tasks:
1. Load / create the dataset.
2. Clean the data.
3. Scale the features using StandardScaler.
4. Train a Feedforward Neural Network model.
5. Evaluate the accuracy of the model.

Input: new_customer = [[46, 1450, 5, 6, 9]]
Expected Output: Customer may leave
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def LoadDataset():
    data = [
        [25, 500, 12, 1, 2],
        [30, 700, 24, 0, 1],
        [45, 1200, 6, 5, 8],
        [50, 1500, 5, 6, 10],
        [28, 600, 18, 1, 1],
        [35, 800, 30, 0, 0],
        [48, 1400, 4, 7, 9],
        [52, 1600, 3, 8, 12],
        [27, 550, 20, 0, 1],
        [42, 1300, 8, 4, 7],
    ]
    labels = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

    df = pd.DataFrame(data, columns=["Age", "MonthlyCharges", "Tenure",
                                     "Complaints", "SupportCalls"])
    df["Churn"] = labels
    df = df.dropna()

    print("Dataset head:")
    print(df.head())
    print("\nDataset info:")
    print(df.info())
    return df


def SplitData(DataFrame):
    X = DataFrame.drop("Churn", axis=1)
    y = DataFrame["Churn"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test, scaler


def TrainModel(X_train, y_train):
    model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000,
                          random_state=42)
    model.fit(X_train, y_train)
    return model


def EvaluateModel(Model, X_test, y_test):
    y_pred = Model.predict(X_test)
    print("\nAccuracy:", accuracy_score(y_test, y_pred))


def PredictCustomer(Model, Scaler):
    new_customer = [[46, 1450, 5, 6, 9]]
    new_scaled = Scaler.transform(new_customer)
    prediction = Model.predict(new_scaled)[0]

    if prediction == 1:
        print("Customer may leave")
    else:
        print("Customer will stay")


def main():
    print("----- Customer Churn Prediction using FNN -----")

    df = LoadDataset()
    X_train, X_test, y_train, y_test, scaler = SplitData(df)

    model = TrainModel(X_train, y_train)
    EvaluateModel(model, X_test, y_test)
    PredictCustomer(model, scaler)


if __name__ == "__main__":
    main()
