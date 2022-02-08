''' 글자 깨지는 한글 파일을 깨지지 않는 버전으로 인코딩'''
import pandas as pd 

df = pd.read_csv('test.csv', header=0)
df.to_csv('test_ko.csv',index=False,encoding='utf-8-sig')