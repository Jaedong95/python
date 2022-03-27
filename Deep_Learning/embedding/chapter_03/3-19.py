'''
Khaiii 클래스 선언 및 형태소 분석, 품사 정보 함께 출력  
'''
from khaiii import KhaiiiApi 

tokenizer = KhaiiiApi()   # Khaiii 클래스 선언 
data = tokenizer.analyze('아버지가방에들어가신다')   # 형태소 분석 수행 
tokens = [] 
for word in data:
    tokens.extend([str(m) for m in word.morphs])    # 형태소 단위로 출력
