"""
Question 7:
Create a scatter plot of Math vs Science marks using Seaborn.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def CreateDataFrame():
    data = {"Name": ["Amit", "Sagar", "Pooja"],
            "Math": [85, 90, 78],
            "Science": [92, 88, 80],
            "English": [75, 85, 82]}

    return pd.DataFrame(data)


def PlotScatterPlot(DataFrame):
    plt.figure()
    sns.scatterplot(data=DataFrame, x="Math", y="Science")
    plt.title("Math vs Science Marks")
    plt.savefig("scatter.png")
    print("Saved scatter.png")


def main():
    print("----- Scatter Plot of Math vs Science -----")

    df = CreateDataFrame()
    PlotScatterPlot(df)


if __name__ == "__main__":
    main()
