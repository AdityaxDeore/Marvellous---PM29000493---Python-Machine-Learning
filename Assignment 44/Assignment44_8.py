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

amit = df[df["Name"] == "Amit"][["Math", "Science", "English"]].iloc[0]

plt.plot(["Math", "Science", "English"], amit.values, marker="o")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Amit's Marks Across Subjects")
plt.savefig("line_plot.png")
print("Saved line_plot.png")
