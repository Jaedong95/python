'''
LDA 피처 생성 
'''
from gensim import corpora 
from preprocess import get_tokenizer

documents, tokenized_corpus = [], [] 

# 토크나이저 생성 
tokenizer = get_tokenizer(tokenizer_name)

with open(corpus_fname, 'r', encoding='utf-8') as f:
    for document in f:   # 문서 단위로 
        # set 자료형을 통해 토큰의 순서를 고려하지 않고, 중복 제거 
        tokens = list(set(tokenizer.morphs(document.strip())))   
        documents.append(document)
        tokenized_corpus.append(tokens)

dictionary = corpora.Dictionary(tokenized_corpus)
corpus = [dictionary.doc2bow(text) for text in tokenized_corpus]