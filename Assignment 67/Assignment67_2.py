import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

data = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1],
]
labels = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]

df = pd.DataFrame(
    data,
    columns=["Income", "CreditScore", "LoanAmount", "ExistingEMI", "EmploymentStatus"],
)
df["Approved"] = labels
df = df.dropna()

print("Dataset head:")
print(df.head())
print("\nDataset info:")
print(df.info())

X = df.drop("Approved", axis=1)
y = df["Approved"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))

new_applicant = [[55000, 720, 400000, 10000, 1]]
new_scaled = scaler.transform(new_applicant)
prediction = model.predict(new_scaled)[0]

if prediction == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")
