import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]}

df = pd.DataFrame(data)
corr = df[['Math', 'Science', 'English']].corr()

plt.figure()
sns.heatmap(corr, annot=True)
plt.title('Correlation between Subject Marks')
plt.savefig('heatmap.png')
print('Saved heatmap.png')
