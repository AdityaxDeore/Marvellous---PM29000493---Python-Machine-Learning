import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Name": ["Amit", "Sagar", "Pooja"],
    "Math": [85, 90, 78],
    "Science": [92, 88, 80],
    "English": [75, 85, 82],
}
df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]

plt.bar(df["Name"], df["Total"])
plt.xlabel("Student")
plt.ylabel("Total Marks")
plt.title("Total Marks per Student")
plt.savefig("bar_plot.png")
print("Saved bar_plot.png")
