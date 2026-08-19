"""
Question 9:
Create a heatmap of correlations between subject marks using Seaborn.
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


def PlotHeatmap(DataFrame):
    corr_matrix = DataFrame[["Math", "Science", "English"]].corr()

    plt.figure()
    sns.heatmap(corr_matrix, annot=True)
    plt.title("Correlation between Subject Marks")
    plt.savefig("heatmap.png")
    print("Saved heatmap.png")


def main():
    print("----- Heatmap of Subject Correlations -----")

    df = CreateDataFrame()
    PlotHeatmap(df)


if __name__ == "__main__":
    main()
