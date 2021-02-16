import pandas as pd

df = pd.read_csv('./KNN/기간별_일평균_대기환경_정보_2018년.csv', encoding='CP949')

#print(df.head())
#print(df.columns)

df.columns = ["cdate","acode","aname","scode","sname","fdust","ufdust","ozone","nd","cm","sagas"]

'''결측값이 nan 으로 표기되어있을 경우 사용하는 방식  
df.dropna(axis=0,how='any')   - 

#print(df.columns)    
#print(df.isnull())
'''

idx = df[df['fdust'] == 0].index
df_1 = df.drop(idx)

# df_1.to_csv('data1.csv',encoding="CP949",index=False)
df_1["airquality"] = "True"

# linear_regression

'''
#print(df_1.head())
df_1["fdust_check"] = df_1["fdust"] > 80   #  True일 경우 미세먼지 농도 나쁨
df_1["ufdust_check"] = df_1["ufdust"] > 35  #  True일 경우 초미세먼지 농도 나쁨
df_1["avg_uf"] = (df_1["fdust"] + df_1["ufdust"]) / 2
# df_1.drop(["bool_test"], axis=1, inplace=True)
'''

def max_value(gas):
    tmp = 0
    for i, d in enumerate(gas):
        if d >= tmp:
            tmp = d
    #print(tmp)
    return tmp

air_dataset = df_1.values
date = air_dataset[:,0]  # date = int형 변수
test = air_dataset[:,5:11]

# print(test[1])
# print(air_dataset[0][-1])

air_quality = []

for i, d in enumerate(test):
    mv = max_value(d)
    if mv >= 0 and mv <= 15:
        air_quality.append("best")
    elif mv >= 16 and mv <= 30:
        air_quality.append("better")
    elif mv >= 31 and mv <= 40:
        air_quality.append("good")
    elif mv >= 41 and mv <= 50:   # 보통
        air_quality.append("normal")
    elif mv >= 51 and mv <= 75:
        air_quality.append("bad")
    elif mv >= 76 and mv <=100:
        air_quality.append("worse")
    elif mv >= 101 and mv <= 150:
        air_quality.append("serious")
    else:
        air_quality.append("worst")

#print(air_quality)

df_1["airquality"] = air_quality
df_1.drop(["ufdust"], axis=1, inplace=True)
print(df_1.head())

# df_1.to_csv('data2.csv',encoding="CP949",index=False)
# print(air_dataset)







