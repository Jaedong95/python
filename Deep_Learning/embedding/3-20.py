'''
은전한닢 분석기를 이용해 가상의 상품평 분석 
'''
from konlpy.tag import Mecab

tokenizer = Mecab() 
tokenizer.morphs('가우스전자 텔레비전 정말 좋네요')