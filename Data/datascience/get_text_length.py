''' 1. 텍스트 데이터 길이 구하는 코드 (공백 x) '''
import pandas as pd 

df = pd.read_csv('../data_in/train.csv',header=0)
df = df.dropna()

text_length = []

def count_token(text):
    list = text.split(' ')
    cnt = len(list)
    
    return cnt 

for i in range(len(df['document'])):
    text_len = count_token(df['document'][i])
    text_length.append(text_len)

df['text_length'] = text_length
df.to_csv('train_bt.csv',index=False,encoding='utf-8-sig')

''' 2. 텍스트 데이터 길이 구하는 코드 (공백 o) '''
import pandas as pd 
import matplotlib as plt 

df = pd.read_csv('../data_in/test.csv',header=0) 
df = df.dropna()

text_length = [] 

for i in range(len(df['document'])):
    length = len(df['document'][i])
    text_length.append(length)

plt.hist(df['text_length'])
plt.show()

df['text_length'] = text_length
df.to_csv('train_bt.csv',index=False,encoding='utf-8-sig')

