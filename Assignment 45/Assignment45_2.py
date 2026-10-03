import pandas as pd
import numpy as np

data2 = {'Name': ['Amit', 'Sagar', 'Pooja'],
         'Math': [np.nan, 76, 88],
         'Science': [91, np.nan, 85]}

df2 = pd.DataFrame(data2)
df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
df2['Science'] = df2['Science'].fillna(df2['Science'].mean())
print(df2)
