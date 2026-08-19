"""
Question 7:
Create a bar plot of student names vs total marks.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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


def PlotBarChart(DataFrame):
    plt.bar(DataFrame["Name"], DataFrame["Total"])
    plt.xlabel("Student")
    plt.ylabel("Total Marks")
    plt.title("Total Marks per Student")
    plt.savefig("bar_plot.png")
    print("Saved bar_plot.png")


def main():
    print("----- Bar Plot of Total Marks -----")

    df = CreateDataFrame()
    AddTotalColumn(df)
    PlotBarChart(df)


if __name__ == "__main__":
    main()
