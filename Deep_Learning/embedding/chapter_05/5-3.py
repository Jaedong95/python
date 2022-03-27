'''
TF-IDF 행렬 구축 
'''
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    min_df = 1,   # DF(Document Frequency)가 1인 단어만 
    ngram_range=(1, 1),  # 유니그램 방식 
    lowercase=True,  
    tokenizer=lambda x: x.split())

input_matrix = vectorizer.fit_transform(noun_corpus)