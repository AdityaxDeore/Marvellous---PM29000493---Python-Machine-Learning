"""
Question 7:
Given the marks dataset, write a program to display the names of students who scored more than 85 in Science.
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


def ShowTopScienceStudents(DataFrame):
    names = DataFrame[DataFrame["Science"] > 85]["Name"].tolist()
    print(names)


def main():
    print("----- Students Scoring Above 85 in Science -----")

    df = CreateDataFrame()
    ShowTopScienceStudents(df)


if __name__ == "__main__":
    main()
