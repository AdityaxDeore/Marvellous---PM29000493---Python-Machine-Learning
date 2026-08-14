"""
Question 9:
Create a DataFrame with 5 students' names and marks in 3 subjects. Display its shape, column names, and data types.
"""

import pandas as pd


def CreateDataFrame():
    data = {
        "Name": ["Amit", "Sagar", "Pooja", "Rahul", "Neha"],
        "Math": [85, 90, 78, 88, 92],
        "Science": [92, 88, 80, 85, 90],
        "English": [75, 85, 82, 79, 88],
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
