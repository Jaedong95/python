'''
단어 벡터 간 유사도 시각화 
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator('/notebooks/embedding/data/word-embeddings/\
    word2vec/word2vec', method='word2vec', dim=100, tokenizer_name='mecab')

# 단어 유사도 평가 데이터셋에 포함된 모든 단어 쌍 간 코사인 유사도를 구하고,
# 이를 Bokeh 라이브러리로 그림으로 출력 
model.visualize_between_words('/notebooks/embedding/data/raw/kor_analogy_semantic.txt')