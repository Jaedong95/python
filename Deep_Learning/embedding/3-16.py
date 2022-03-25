''' 
꼬꼬마, 한나눔, Okt 등 KoNLPy에 속한 다른 형태소 분석기 중 
사용하고 싶은 분석기를 전달받아 반환 
'''
from konlpy.tag import Okt, Komoran, Mecab, Hannanum, Kkma

def get_tokenizer(tokenizer_name):
    if tokenizer_name == "komoran":   # 코모란 형태소 분석기 
        tokenizer = Komoran()
    elif tokenizer_name == "okt":   # Okt 형태소 분석기 
        tokenizer = Okt()
    elif tokenizer_name == "mecab":   # 은전한닢 형태소 분석기 
        tokenizer = Mecab()
    elif tokenizer_name == "hannanum":   # 한나눔 형태소 분석기 
        tokenizer = Hannanum()
    elif tokenizer_name == "kkma":   # kkma 형태소 분석기 
        tokenizer = Kkma()
#    elif tokenizer_name == "khaiii":
#        tokenizer = KhaiiiApi()
    else:
        tokenizer = Mecab()
    return tokenizer
