'''
단어 유추 평가 수행 코드 
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator('/notebooks/embedding/data/word-embeddings/\
    word2vec/word2vec', method='word2vec', dim=100, tokenizer_name='mecab')

model.word_analogy_test('data/raw/kor_analogy_semantic.txt', verbose=False)