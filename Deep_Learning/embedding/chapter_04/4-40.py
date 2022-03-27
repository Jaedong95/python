'''
단어 임베딩의 t-SNE 2차원 시각화 
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator('/notebooks/embedding/data/word-embeddings/\
    word2vec/word2vec', method='word2vec', dim=100, tokenizer_name='mecab')

model.visualize_words('/notebooks/embedding/data/raw/kor_analogy_semantic.txt')