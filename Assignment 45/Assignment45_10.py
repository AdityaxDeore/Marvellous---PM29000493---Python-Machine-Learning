"""
Question 10:
Drop the 'English' column and display the updated DataFrame.
"""

import pandas as pd


def CreateDataFrame():
    data = {"Name": ["Amit", "Sagar", "Pooja"],
            "Math": [85, 90, 78],
            "Science": [92, 88, 80],
            "English": [75, 85, 82]}

    return pd.DataFrame(data)


def DropColumn(DataFrame):
    return DataFrame.drop("English", axis=1)


def main():
    print("----- Drop English Column -----")

    df = CreateDataFrame()
    df = DropColumn(df)
    print(df)


if __name__ == "__main__":
    main()
