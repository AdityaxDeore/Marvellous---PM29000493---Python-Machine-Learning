"""
Question 9:
Create a DataFrame with missing values and fill them with column mean.
"""

import numpy as np
import pandas as pd


def CreateDataFrame():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [np.nan, 76, 88],
        "Science": [91, np.nan, 85],
    }

    return pd.DataFrame(data)


def FillMissingValues(DataFrame):
    return DataFrame.fillna(DataFrame.mean(numeric_only=True))


def main():
    print("----- Fill Missing Values with Column Mean -----")

    df = CreateDataFrame()

    print("Before:")
    print(df)

    df = FillMissingValues(df)

    print("\nAfter filling with column mean:")
    print(df)


if __name__ == "__main__":
    main()
