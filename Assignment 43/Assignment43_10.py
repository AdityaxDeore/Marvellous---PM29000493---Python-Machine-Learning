import numpy as np
import pandas as pd

data = {
    "Name": ["Amit", "Sagar", "Pooja", "Rahul"],
    "Math": [85, np.nan, 78, 88],
    "Science": [92, 88, np.nan, 85],
    "English": [75, 85, 82, np.nan],
}
df = pd.DataFrame(data)

print("Missing values per column:")
print(df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))

print("\nAfter filling with column mean:")
print(df)

print("\nWhy it matters: most ML models cannot handle NaN values and will fail or "
      "produce wrong results. Filling with the column mean keeps the row usable "
      "without shifting the feature's average, giving the model clean, complete data.")
