"""
Question 1:
Using the same dataset 'data' from the previous assignment, calculate the average marks for each subject.
"""

import pandas as pd


def CreateDataFrame():
    data = {"Name": ["Amit", "Sagar", "Pooja"],
            "Math": [85, 90, 78],
            "Science": [92, 88, 80],
            "English": [75, 85, 82]}

    return pd.DataFrame(data)


def ShowAverageMarks(DataFrame):
    avg_marks = DataFrame[["Math", "Science", "English"]].mean()
    print(avg_marks)


def main():
    print("----- Average Marks Per Subject -----")

    df = CreateDataFrame()
    ShowAverageMarks(df)


if __name__ == "__main__":
    main()
