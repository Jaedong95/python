import pandas as pd 

csv_names = ['./melon.csv', './bugs.csv', './Genie.csv']
appended_data = pd.DataFrame()

for name in csv_names:
    pd_data = pd.read_csv(name)
    appended_data = appended_data.append(pd_data)

print(appended_data.info())

appended_data.to_csv('./total_rank.csv',index=False)