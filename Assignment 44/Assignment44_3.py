"""
Question 3:
Add a new column 'Total' to the DataFrame as the sum of all subject marks.
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


def AddTotalColumn(DataFrame):
    DataFrame["Total"] = DataFrame["Math"] + DataFrame["Science"] + DataFrame["English"]


def main():
    print("----- Add Total Marks Column -----")

    df = CreateDataFrame()
    AddTotalColumn(df)
    print(df)


if __name__ == "__main__":
    main()
