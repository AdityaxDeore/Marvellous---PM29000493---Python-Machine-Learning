"""
Question 5:
Using Pandas, load a CSV dataset and display the first 5 rows, last 5 rows, and basic information (columns, data types).
"""

import pandas as pd


def CreateCSV(FileName):
    data = {
        "Name": ["Amit", "Sagar", "Pooja", "Rahul", "Neha"],
        "Math": [85, 90, 78, 88, 92],
        "Science": [92, 88, 80, 85, 90],
        "English": [75, 85, 82, 79, 88],
    }

    pd.DataFrame(data).to_csv(FileName, index=False)


def ShowDataInfo(DataFrame):
    print("First 5 rows:")
    print(DataFrame.head())

    print("\nLast 5 rows:")
    print(DataFrame.tail())

    print("\nColumns:", list(DataFrame.columns))

    print("\nData types:")
    print(DataFrame.dtypes)


def main():
    print("----- Load and Explore CSV Dataset -----")

    file_name = "student_marks.csv"

    CreateCSV(file_name)
    df = pd.read_csv(file_name)
    ShowDataInfo(df)


if __name__ == "__main__":
    main()
