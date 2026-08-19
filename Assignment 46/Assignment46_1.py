"""
Question:
Advertisement Sales Prediction Using Linear Regression.
Analyze the advertising expenditure of a company and predict its total sales.

Steps:
1. Load the dataset 'Advertisement.csv' using Pandas.
2. Perform the exploratory data analysis (EDA).
3. Split the dataset into training and testing parts.
4. Train the Linear Regression model.
5. Test the model and evaluate its performance.
6. Predict the sales for a new input and display it.

Expected Output: Model equation, coefficients, R2, MSE, RMSE and
predicted sales for TV=150, Radio=30, Newspaper=25.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def LoadDataset(FileName):
    df = pd.read_csv(FileName)
    df = df.drop(columns=[c for c in df.columns if "Unnamed" in c])
    return df


def DoEDA(DataFrame):
    print(DataFrame.head())
    print(DataFrame.info())
    print(DataFrame.describe())
    print("Correlation with sales:\n", DataFrame.corr()["sales"])

    plt.figure(figsize=(15, 4))
    for i, col in enumerate(["TV", "radio", "newspaper"], 1):
        plt.subplot(1, 3, i)
        plt.scatter(DataFrame[col], DataFrame["sales"])
        plt.xlabel(col)
        plt.ylabel("sales")
        plt.title(f"{col} vs sales")
    plt.tight_layout()
    plt.savefig("advertising_scatter.png")
    plt.close()

    plt.figure(figsize=(6, 5))
    plt.imshow(DataFrame.corr(), cmap="coolwarm")
    plt.xticks(range(4), DataFrame.columns, rotation=45)
    plt.yticks(range(4), DataFrame.columns)
    plt.colorbar()
    plt.title("Correlation heatmap")
    plt.tight_layout()
    plt.savefig("advertising_corr.png")
    plt.close()


def SplitData(DataFrame):
    X = DataFrame[["TV", "radio", "newspaper"]]
    y = DataFrame["sales"]
    return train_test_split(X, y, test_size=0.2, random_state=42)


def TrainModel(XTrain, YTrain):
    model = LinearRegression()
    model.fit(XTrain, YTrain)
    return model


def EvaluateModel(Model, XTest, YTest):
    y_pred = Model.predict(XTest)
    r2 = r2_score(YTest, y_pred)
    mse = mean_squared_error(YTest, y_pred)
    rmse = np.sqrt(mse)
    return y_pred, r2, mse, rmse


def PredictSales(Model, TV, Radio, Newspaper):
    new = pd.DataFrame([[TV, Radio, Newspaper]],
                       columns=["TV", "radio", "newspaper"])
    return Model.predict(new)[0]


def CreatePDFReport(Equation, Coef, Intercept, R2, MSE, RMSE, PredSales):
    lines = [
        "Marvellous Infosystems : Python - Automation & Machine Learning",
        "Machine Learning Assignment 46",
        "Advertisement Sales Prediction Using Linear Regression",
        "",
        "Q1. What is the mathematical equation of your trained Linear Regression model?",
        "",
        Equation,
        "",
        "Q2. What are the values of your model's coefficient (m) and intercept (c)?",
        "",
        f"Coefficients: TV = {Coef[0]:.4f}, radio = {Coef[1]:.4f}, newspaper = {Coef[2]:.4f}",
        f"Intercept (c) = {Intercept:.4f}",
        "",
        "Q3. Display the values of R2 score, Mean Squared Error (MSE),",
        "and Root Mean Squared Error (RMSE) for your model.",
        "",
        f"R2 score = {R2:.4f}",
        f"MSE = {MSE:.4f}",
        f"RMSE = {RMSE:.4f}",
        "",
        "Q4. Predict the sales for TV=150, Radio=30, and Newspaper=25",
        "and display the predicted value.",
        "",
        f"Predicted sales = {PredSales:.4f}",
    ]
    with PdfPages("Assignment_46.pdf") as pdf:
        plt.figure(figsize=(8.5, 11))
        plt.axis("off")
        plt.text(0.05, 0.95, "\n".join(lines), fontsize=11, va="top",
                 ha="left", family="monospace",
                 transform=plt.gca().transAxes)
        pdf.savefig()
        plt.close()


def main():
    print("----- Advertisement Sales Prediction Using Linear Regression -----")

    df = LoadDataset("Advertisement.csv")
    DoEDA(df)

    x_train, x_test, y_train, y_test = SplitData(df)
    model = TrainModel(x_train, y_train)

    coef = model.coef_
    intercept = model.intercept_

    y_pred, r2, mse, rmse = EvaluateModel(model, x_test, y_test)
    pred_sales = PredictSales(model, 150, 30, 25)

    equation = (f"sales = {coef[0]:.4f}*TV + {coef[1]:.4f}*radio + "
                f"{coef[2]:.4f}*newspaper + {intercept:.4f}")

    print("\nModel equation:", equation)
    print("Coefficients:", coef)
    print("Intercept:", intercept)
    print(f"R2: {r2:.4f}, MSE: {mse:.4f}, RMSE: {rmse:.4f}")
    print(f"Predicted sales for TV=150, Radio=30, Newspaper=25: {pred_sales:.4f}")

    CreatePDFReport(equation, coef, intercept, r2, mse, rmse, pred_sales)
    print("Saved: Assignment_46.pdf, advertising_scatter.png, advertising_corr.png")


if __name__ == "__main__":
    main()
