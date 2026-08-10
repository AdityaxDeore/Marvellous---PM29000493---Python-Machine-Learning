"""
Question 3:
Create a Pandas DataFrame with the following data:

Name    Age    City      Score
Amit    25     Pune      88
Rohan   22     Mumbai    75
Priya   28     Delhi     92
Rahul   24     Pune      67

Perform the following operations using Pandas:
- Display the first 3 rows.
- Display the last 2 rows.
- Print column names and data types.
- Filter students with Score greater than 80.
- Add a new column 'Result' with 'Pass' if Score >= 75, else 'Fail'.

Note: Use DataFrame operations like head(), tail(), info(), filtering and
column creation.
"""

import pandas as pd


def CreateDataFrame():
    data = {"Name": ["Amit", "Rohan", "Priya", "Rahul"],
            "Age": [25, 22, 28, 24],
            "City": ["Pune", "Mumbai", "Delhi", "Pune"],
            "Score": [88, 75, 92, 67]}

    df = pd.DataFrame(data)
    return df


def AddResultColumn(DataFrame):
    results = []
    for score in DataFrame["Score"]:
        if score >= 75:
            results.append("Pass")
        else:
            results.append("Fail")
    DataFrame["Result"] = results


def DisplayInfo(DataFrame):
    print("First 3 rows:\n", DataFrame.head(3))
    print("\nLast 2 rows:\n", DataFrame.tail(2))
    print("\nColumn names:", list(DataFrame.columns))
    print("\nData types:\n", DataFrame.dtypes)

    print("\nStudents with Score greater than 80:\n", DataFrame[DataFrame["Score"] > 80])

    AddResultColumn(DataFrame)
    print("\nDataFrame with Result column:\n", DataFrame)


def main():
    df = CreateDataFrame()
    DisplayInfo(df)


if __name__ == "__main__":
    main()
