"""
Question 2:
Create a DataFrame 'data2' with missing values and fill them using the column mean.
"""

import pandas as pd
import numpy as np


def CreateDataFrame():
    data = {"Name": ["Amit", "Sagar", "Pooja"],
            "Math": [np.nan, 76, 88],
            "Science": [91, np.nan, 85]}

    return pd.DataFrame(data)


def FillMissingValues(DataFrame):
    # Fill each column with its own mean
    DataFrame["Math"] = DataFrame["Math"].fillna(DataFrame["Math"].mean())
    DataFrame["Science"] = DataFrame["Science"].fillna(DataFrame["Science"].mean())


def main():
    print("----- Fill Missing Values with Column Mean -----")

    df = CreateDataFrame()
    FillMissingValues(df)
    print(df)


if __name__ == "__main__":
    main()
