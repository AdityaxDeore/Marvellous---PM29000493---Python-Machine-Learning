"""
Question 4:
Create a box plot for subject marks using Seaborn.
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


def PlotBoxPlot(DataFrame):
    plt.figure()
    sns.boxplot(data=DataFrame[["Math", "Science", "English"]])
    plt.title("Subject Marks Distribution")
    plt.savefig("box_plot.png")
    print("Saved box_plot.png")


def main():
    print("----- Box Plot of Subject Marks -----")

    df = CreateDataFrame()
    PlotBoxPlot(df)


if __name__ == "__main__":
    main()
