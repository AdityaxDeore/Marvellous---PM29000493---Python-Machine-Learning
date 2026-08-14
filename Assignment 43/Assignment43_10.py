"""
Question 10:
Write a Python program to check if the dataset contains any missing values. If missing values exist, replace them with the mean of the respective column. Also, explain why handling missing values is important before model training.
"""

import numpy as np
import pandas as pd


def CreateDataFrame():
    data = {
        "Name": ["Amit", "Sagar", "Pooja", "Rahul"],
        "Math": [85, np.nan, 78, 88],
        "Science": [92, 88, np.nan, 85],
        "English": [75, 85, 82, np.nan],
    }

    return pd.DataFrame(data)


def ShowMissingValues(DataFrame):
    print("Missing values per column:")
    print(DataFrame.isnull().sum())


def FillMissingValues(DataFrame):
    return DataFrame.fillna(DataFrame.mean(numeric_only=True))


def main():
    print("----- Handle Missing Values -----")

    df = CreateDataFrame()

    ShowMissingValues(df)

    df = FillMissingValues(df)

    print("\nAfter filling with column mean:")
    print(df)

    # Most ML models cannot handle NaN values and will fail or
    # give wrong results, so we fill them with the column mean.
    print("\nWhy it matters: most ML models cannot handle NaN values and will fail or "
          "produce wrong results. Filling with the column mean keeps the row usable "
          "without shifting the feature's average, giving the model clean, complete data.")


if __name__ == "__main__":
    main()
