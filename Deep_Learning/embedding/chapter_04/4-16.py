'''
미등록 단어에 대한 자소 단위 FastText 임베딩 체크 
'''
from models.word_eval import WordEmbeddingEvaluator 

model = WordEmbeddingEvaluator(
    vecs_txt_fname='/notebooks/embedding/data/word-embeddings/\
        fasttext-jamo/fasttext-jamo.vec',
    vecs_bin_fname= '/notebooks/embedding/data/word-embeddings/\
        fasttext-jamo/fasttext-jamo.bin',
    method = 'fasttext-jamo', dim=100, tokenizer_name='mecab')

model._is_in_vocabulary('서울특별시')   # 단어가 등록되어 있는지 체크 
model.get_word_vector('서울특별시')   # 단어 벡터를 가져옴 
model.most_similar('서울특별시', topn=5)   # 미등록 단어 테스트