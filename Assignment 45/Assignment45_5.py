"""
Question 5:
Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'.
"""

import pandas as pd


def CreateDataFrame():
    data = {"Name": ["Amit", "Sagar", "Pooja"],
            "Math": [85, 90, 78],
            "Science": [92, 88, 80],
            "English": [75, 85, 82]}

    return pd.DataFrame(data)


def AddTotalColumn(DataFrame):
    DataFrame["Total"] = DataFrame["Math"] + DataFrame["Science"] + DataFrame["English"]


def AddStatusColumn(DataFrame):
    status = []

    for total in DataFrame["Total"]:
        if total >= 250:
            status.append("Pass")
        else:
            status.append("Fail")

    DataFrame["Status"] = status


def main():
    print("----- Add Pass or Fail Status -----")

    df = CreateDataFrame()
    AddTotalColumn(df)
    AddStatusColumn(df)
    print(df)


if __name__ == "__main__":
    main()
