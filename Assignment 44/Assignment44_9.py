import numpy as np
import pandas as pd

data2 = {
    "Name": ["Amit", "Sagar", "Pooja"],
    "Math": [np.nan, 76, 88],
    "Science": [91, np.nan, 85],
}
df = pd.DataFrame(data2)

print("Before:")
print(df)

df = df.fillna(df.mean(numeric_only=True))

print("\nAfter filling with column mean:")
print(df)
