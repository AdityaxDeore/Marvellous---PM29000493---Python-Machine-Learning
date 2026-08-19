"""
Question 6:
Create a histogram of total marks using Matplotlib.
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


def AddTotalColumn(DataFrame):
    DataFrame["Total"] = DataFrame["Math"] + DataFrame["Science"] + DataFrame["English"]


def PlotHistogram(DataFrame):
    plt.figure()
    plt.hist(DataFrame["Total"])
    plt.xlabel("Total Marks")
    plt.ylabel("Frequency")
    plt.title("Histogram of Total Marks")
    plt.savefig("hist_total.png")
    print("Saved hist_total.png")


def main():
    print("----- Histogram of Total Marks -----")

    df = CreateDataFrame()
    AddTotalColumn(df)
    PlotHistogram(df)


if __name__ == "__main__":
    main()
