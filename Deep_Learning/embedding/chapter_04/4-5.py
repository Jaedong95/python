'''
코사인 유사도 상위 단어 목록 체크 코드와 결과 예시 
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator('/notebooks/embedding/data/word-embeddings/\
    word2vec/word2vec', method='word2vec', dim=100, tokenizer_name='mecab')

model.most_similar('희망', topn=5)

