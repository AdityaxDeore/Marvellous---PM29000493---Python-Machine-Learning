import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# 1. Load dataset
df = pd.read_csv("Advertisement.csv")
df = df.drop(columns=[c for c in df.columns if "Unnamed" in c])

# 2. Exploratory data analysis
print(df.head())
print(df.info())
print(df.describe())
print("Correlation with sales:\n", df.corr()["sales"])

plt.figure(figsize=(15, 4))
for i, col in enumerate(["TV", "radio", "newspaper"], 1):
    plt.subplot(1, 3, i)
    plt.scatter(df[col], df["sales"])
    plt.xlabel(col)
    plt.ylabel("sales")
    plt.title(f"{col} vs sales")
plt.tight_layout()
plt.savefig("advertising_scatter.png")
plt.close()

plt.figure(figsize=(6, 5))
plt.imshow(df.corr(), cmap="coolwarm")
plt.xticks(range(4), df.columns, rotation=45)
plt.yticks(range(4), df.columns)
plt.colorbar()
plt.title("Correlation heatmap")
plt.tight_layout()
plt.savefig("advertising_corr.png")
plt.close()

# 3. Train-test split
X = df[["TV", "radio", "newspaper"]]
y = df["sales"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

coef = model.coef_
intercept = model.intercept_

# 5. Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# 6. Predict sales for a new input
new = pd.DataFrame([[150, 30, 25]], columns=["TV", "radio", "newspaper"])
pred_sales = model.predict(new)[0]

equation = (f"sales = {coef[0]:.4f}*TV + {coef[1]:.4f}*radio + "
            f"{coef[2]:.4f}*newspaper + {intercept:.4f}")

print("\nModel equation:", equation)
print("Coefficients:", coef)
print("Intercept:", intercept)
print(f"R2: {r2:.4f}, MSE: {mse:.4f}, RMSE: {rmse:.4f}")
print(f"Predicted sales for TV=150, Radio=30, Newspaper=25: {pred_sales:.4f}")

# 7. Write the expected PDF deliverable with the actual computed values
with PdfPages("Assignment_46.pdf") as pdf:
    plt.figure(figsize=(8.5, 11))
    plt.axis("off")
    lines = [
        "Marvellous Infosystems : Python - Automation & Machine Learning",
        "Machine Learning Assignment 46",
        "Advertisement Sales Prediction Using Linear Regression",
        "",
        "Q1. What is the mathematical equation of your trained Linear Regression model?",
        "",
        equation,
        "",
        "Q2. What are the values of your model's coefficient (m) and intercept (c)?",
        "",
        f"Coefficients: TV = {coef[0]:.4f}, radio = {coef[1]:.4f}, newspaper = {coef[2]:.4f}",
        f"Intercept (c) = {intercept:.4f}",
        "",
        "Q3. Display the values of R2 score, Mean Squared Error (MSE),",
        "and Root Mean Squared Error (RMSE) for your model.",
        "",
        f"R2 score = {r2:.4f}",
        f"MSE = {mse:.4f}",
        f"RMSE = {rmse:.4f}",
        "",
        "Q4. Predict the sales for TV=150, Radio=30, and Newspaper=25",
        "and display the predicted value.",
        "",
        f"Predicted sales = {pred_sales:.4f}",
    ]
    plt.text(0.05, 0.95, "\n".join(lines), fontsize=11, va="top", ha="left",
             family="monospace", transform=plt.gca().transAxes)
    pdf.savefig()
    plt.close()

print("Saved: Assignment_46.pdf, advertising_scatter.png, advertising_corr.png")
