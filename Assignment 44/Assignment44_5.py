"""
Question 5:
Replace 'Pooja' with 'Puja' in the 'Name' column.
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


def ReplaceName(DataFrame):
    DataFrame["Name"] = DataFrame["Name"].replace("Pooja", "Puja")


def main():
    print("----- Replace Student Name -----")

    df = CreateDataFrame()
    ReplaceName(df)
    print(df)


if __name__ == "__main__":
    main()
