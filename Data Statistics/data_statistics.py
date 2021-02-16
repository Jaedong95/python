import pandas as pd 

df = pd.read_csv('./diabetes.csv',names=["pregnant","plasma","bp","thickness","Insulin","bmi","pdigree","age","class"],skiprows=1)
# print(df.head(5))
# print(df.info())
# print(df.describe())
# print(df[['plasma','thickness','bmi','class']])
# print(df[['age','class']].groupby(['age'], as_index=False).mean().sort_values(by='age',ascending=True))

'''
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,12))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white',annot=True)

plt.show()

grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'bmi',bins=10)
plt.show()
'''

import numpy as np

dataset = np.loadtxt('./diabetes.csv',delimiter=',',skiprows=1)
print(dataset)