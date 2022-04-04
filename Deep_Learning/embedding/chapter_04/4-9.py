'''
FastText Skip-gram 모델의 코사인 유사도 상위 단어 목록 체크 
'''
from models.word_eval import WordEmbeddingEvaluator 
asda
model = WordEmbeddingEvaluator(
    vecs_txt_fname='/notebooks/embedding/data/word-embeddings/\
        fasttext/fasttext.vec',
    vecs_bin_fname='/notebooks/embedding/data/word-embeddings/\
        fasttext/fasttext.bin',
    method='fasttext', dim=100, tokenizer_name='mecab')

model.most_similar('희망', topn=5)   # 희망과 유사도가 높은 상위 단어 5개 