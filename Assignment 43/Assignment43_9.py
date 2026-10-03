import pandas as pd

data = {
    "Name": ["Amit", "Sagar", "Pooja", "Rahul", "Neha"],
    "Math": [85, 90, 78, 88, 92],
    "Science": [92, 88, 80, 85, 90],
    "English": [75, 85, 82, 79, 88],
}
df = pd.DataFrame(data)

print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Data types:")
print(df.dtypes)
