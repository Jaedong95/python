'''
Swivel 모델의 코사인 유사도 상위 목록 체크
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator('/notebooks/embedding/data/word-embeddings/\
    swivel/row_embeddings.tsv', method='swivel', dim=100, tokenizer_name='mecab')

model.most_similar('희망', topn=5)