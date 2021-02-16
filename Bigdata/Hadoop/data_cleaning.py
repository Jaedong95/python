import pandas as pd

df = pd.read_csv('./hw_01/AL_41_D003_20200520.csv', encoding='CP949')

#print(df.head())
#print(df.columns)

df.columns = ["id","dongcode","dongname","areano","bookcode","book","landtype","landtypename","area","ownertype","ownertypename","ownercount","scalecode","scalename","datadate"]

''' 결측값이 nan 으로 표기되어 있을 경우 사용'''
df.dropna(how='any')

#print(df.columns)

df.to_csv('bigdata1.csv',index=False,encoding='CP949')