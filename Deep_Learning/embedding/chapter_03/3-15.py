''' 
은전한닢 형태소 분석기를 이용한 형태소 분석 + 품사 출력   
'''
from konlpy.tag import Mecab()

tokenizer = Mecab() 
tokenizer.pos('아버지가방에들어가신다')   # 품사까지 확인 