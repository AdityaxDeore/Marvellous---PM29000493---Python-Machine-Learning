"""
Question 8:
Plot a line chart of marks for 'Amit' across all subjects.
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


def PlotLineChart(DataFrame):
    amit = DataFrame[DataFrame["Name"] == "Amit"][["Math", "Science", "English"]].iloc[0]

    plt.plot(["Math", "Science", "English"], amit.values, marker="o")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("Amit's Marks Across Subjects")
    plt.savefig("line_plot.png")
    print("Saved line_plot.png")


def main():
    print("----- Line Chart of Amit's Marks -----")

    df = CreateDataFrame()
    PlotLineChart(df)


if __name__ == "__main__":
    main()
