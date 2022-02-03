from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd

df = pd.read_csv('./bigdata2.csv',header=None)
area_dataset = df.values

landtype_name = area_dataset[:,0]
sum_area = area_dataset[:,1]

font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/NGULIM.ttf').get_name()
rc('font',family=font_name)
plt.rcParams["font.size"] = 10
#print(df.head())
#print(landtype_name)

plt.pie(sum_area,labels=landtype_name,autopct='%1.1f%%')
plt.axis('equal')
plt.title("<경기도 지목명별 면적의 비율>",color='darkblue')
plt.show()