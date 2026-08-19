"""
Question 3:
Create a bar plot showing average marks per subject using Matplotlib.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def CreateDataFrame():
    data = {"Name": ["Amit", "Sagar", "Pooja"],
            "Math": [85, 90, 78],
            "Science": [92, 88, 80],
            "English": [75, 85, 82]}

    return pd.DataFrame(data)


def PlotBarChart(DataFrame):
    avg_marks = DataFrame[["Math", "Science", "English"]].mean()

    plt.figure()
    plt.bar(avg_marks.index, avg_marks.values)
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.title("Average Marks per Subject")
    plt.savefig("avg_bar.png")
    print("Saved avg_bar.png")


def main():
    print("----- Bar Plot of Average Marks -----")

    df = CreateDataFrame()
    PlotBarChart(df)


if __name__ == "__main__":
    main()
