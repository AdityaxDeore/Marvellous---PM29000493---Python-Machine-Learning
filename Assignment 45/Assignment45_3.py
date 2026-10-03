import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

data = {'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]}

df = pd.DataFrame(data)
avg = df[['Math', 'Science', 'English']].mean()

plt.figure()
plt.bar(avg.index, avg.values)
plt.xlabel('Subject')
plt.ylabel('Average Marks')
plt.title('Average Marks per Subject')
plt.savefig('avg_bar.png')
print('Saved avg_bar.png')
