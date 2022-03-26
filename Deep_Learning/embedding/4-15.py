'''
FastText Skip-gram 모델의 유사어 상위 목록 체크 
앞선 코드에 쿼리 단어의 자소 변환과 상위 유사 단어의 음절 원복 과정 추가됨
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator(
    vecs_txt_fname='/notebooks/embedding/data/word-embeddings/\
        fasttext-jamo/fasttext-jamo.vec',
    vecs_bin_fname= '/notebooks/embedding/data/word-embeddings/\
        fasttext-jamo/fasttext-jamo.bin',
    method = 'fasttext-jamo', dim=100, tokenizer_name='mecab')

model.most_similar('희망')