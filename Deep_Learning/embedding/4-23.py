'''
코사인 유사도 상위 단어 목록 체크 (PPMI + LSA)
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator('/notebooks/embedding/data/word-embeddings/\
    lsa/lsa-pmi.vecs', method='lsa', dim=100, tokenizer_name='mecab')

model.most_similar('희망', topn=5)