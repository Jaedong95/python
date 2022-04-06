'''
데이터 불러오기, 저장하기 
'''
# 0. 데이터 읽어오기 
import pandas as pd 

pd.read_csv('~.csv', 

# 1. 데이터 저장하기 
df.to_csv('~.csv', index=None) 



# n. 데이터 구조 확인  
df[
df[col].unique()   # 컬럼 내 고유값들 리스트로 반환 
df[col].value_counts() 

# n. 데이터프레임에서 무작위로 행 추출 
import random 

x = random.sample(10000, 100)   # 1 ~ 10,000 사이의 정수 무작위로 100개 추출 (중복 x)

df2 = df1.copy()  # 추출할 테이블 복사본 생성 
df2 = df2.loc[x]   # 앞에서 생성한 x에 해당하는 인덱스들 저장 

# n. 데이터프레임 정렬 
df.sort_values(by='col1') 

# n. 데이터프레임 필터링
filter = df['col1'] > 19 

df = df[filter] 

# n. 데이터프레임 컬럼 이름 재설정 
col_name = ['a', 'b', 'c', ... 'n']

df.columns = col_name 

# 데이터프레임 병합 
df3 = pd.merge(df1, df2m on='col1')   # 공통되는 컬럼(col1) 지정 
