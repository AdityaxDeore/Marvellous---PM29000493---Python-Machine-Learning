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

plt.figure()
sns.scatterplot(data=df, x='Math', y='Science')
plt.title('Math vs Science Marks')
plt.savefig('scatter.png')
print('Saved scatter.png')
