'''
Khaiii 클래스 선언 및 형태소 분석 
'''
from khaiii import KhaiiiApi 

tokenizer = KhaiiiApi()   # Khaiii 클래스 선언 

data = tokenizer.analyze('아버지가방에들어가신다')   # 형태소 분석 수행 
tokens = [] 
for word in data:
    # 형태소 분석 결과를 '/'로 분리한 후 앞부분만 출력 
    tokens.extend([str(m).split('/')[0] for m in word.morphs])  