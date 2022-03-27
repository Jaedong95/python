'''
한글 자소분해 예시 
'''
from preprocess import jamo_sentence, get_tokenizer 

tokenizer = get_tokenizer('mecab')   # 은전한닢 형태소 분석기 생성
tokens = ' '.join(tokenizer.morphs('나는 학교에 간다'))   # 형태소 분석 수행 
print(jamo_sentence(tokens))   # 한글 한 글자를 초성, 중성, 종성 셋으로 분리 