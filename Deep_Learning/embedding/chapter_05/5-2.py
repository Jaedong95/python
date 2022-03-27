'''
학습 데이터 전처리
'''
from preprocess import get_tokenizer 

corpus_fname = 'data/processed/processed_blog.txt'

tokenizer = get_tokenizer('mecab')   # 은전한닢 형태소 분석기 생성 
titles, raw_corpus, noun_corpus = [], [], [] 
with open(corpus_fname, 'r', encoding='utf-8') as f: 
    for line in f:   # 매 줄마다 
        try: 
            title, document = line.strip().split('\u241E')   # 제목, 문서 분리
            titles.append(title)    
            raw_corpus.append(document)   # 문서 추가 
            nouns = tokenizer.nouns(document)   # 명사만 추출 
            noun_corpus.append(' '.join(nouns))
        except:
            continue
