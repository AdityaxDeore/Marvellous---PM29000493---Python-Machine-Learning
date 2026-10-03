import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

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

df = pd.DataFrame(data, columns=["Age", "MonthlyCharges", "Tenure", "Complaints", "SupportCalls"])
df["Churn"] = labels
df = df.dropna()

print("Dataset head:")
print(df.head())
print("\nDataset info:")
print(df.info())

X = df.drop("Churn", axis=1)
y = df["Churn"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))

new_customer = [[46, 1450, 5, 6, 9]]
new_scaled = scaler.transform(new_customer)
prediction = model.predict(new_scaled)[0]

if prediction == 1:
    print("Customer may leave")
else:
    print("Customer will stay")
