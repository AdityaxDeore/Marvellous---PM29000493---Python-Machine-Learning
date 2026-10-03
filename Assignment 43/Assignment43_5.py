import pandas as pd

data = {
    "Name": ["Amit", "Sagar", "Pooja", "Rahul", "Neha"],
    "Math": [85, 90, 78, 88, 92],
    "Science": [92, 88, 80, 85, 90],
    "English": [75, 85, 82, 79, 88],
}
pd.DataFrame(data).to_csv("student_marks.csv", index=False)

df = pd.read_csv("student_marks.csv")

print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("\nColumns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
