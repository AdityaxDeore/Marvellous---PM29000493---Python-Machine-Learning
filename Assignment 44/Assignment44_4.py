"""
Question 4:
Display students who scored more than 85 in Science.
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


def FilterStudents(DataFrame):
    return DataFrame[DataFrame["Science"] > 85]


def main():
    print("----- Students Scoring Above 85 in Science -----")

    df = CreateDataFrame()
    result = FilterStudents(df)
    print(result)


if __name__ == "__main__":
    main()
