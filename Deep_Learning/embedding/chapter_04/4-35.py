'''
단어 유사도 평가 수행 코드 
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator('/notebooks/embedding/data/word-embeddings/\
    word2vec/word2vec', method='word2vec', dim=100, tokenizer_name='mecab')

model.most_similar('희망', topn=5)