"""
Question 2:
Use the DataFrame from Q1 and print descriptive statistics using .describe().
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


def ShowStatistics(DataFrame):
    print(DataFrame.describe())


def main():
    print("----- Descriptive Statistics -----")

    df = CreateDataFrame()
    ShowStatistics(df)


if __name__ == "__main__":
    main()
