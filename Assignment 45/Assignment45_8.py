"""
Question 8:
Create a pairplot of subject marks using Seaborn.
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


def PlotPairPlot(DataFrame):
    graph = sns.pairplot(DataFrame[["Math", "Science", "English"]])
    graph.savefig("pairplot.png")
    print("Saved pairplot.png")


def main():
    print("----- Pairplot of Subject Marks -----")

    df = CreateDataFrame()
    PlotPairPlot(df)


if __name__ == "__main__":
    main()
