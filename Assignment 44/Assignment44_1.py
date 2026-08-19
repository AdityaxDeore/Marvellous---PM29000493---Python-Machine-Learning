"""
Question 1:
Create a DataFrame for student marks and print basic information like shape, columns, and data types.
"""

import pandas as pd


def CreateDataFrame():
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82],
    }

    return pd.DataFrame(data)


def ShowDataInfo(DataFrame):
    print("Shape:", DataFrame.shape)
    print("Columns:", list(DataFrame.columns))
    print("Data types:")
    print(DataFrame.dtypes)


def main():
    print("----- Student Marks DataFrame -----")

    df = CreateDataFrame()
    ShowDataInfo(df)


if __name__ == "__main__":
    main()
