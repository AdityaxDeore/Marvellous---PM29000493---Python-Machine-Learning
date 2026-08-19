"""
Question 6:
Sort the DataFrame by 'Total' marks in descending order.
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


def SortByTotal(DataFrame):
    return DataFrame.sort_values("Total", ascending=False)


def main():
    print("----- Sort Students by Total Marks -----")

    df = CreateDataFrame()
    AddTotalColumn(df)
    df = SortByTotal(df)
    print(df)


if __name__ == "__main__":
    main()
