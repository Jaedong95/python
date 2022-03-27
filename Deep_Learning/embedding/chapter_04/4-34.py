'''
평가 클래스 로드 
'''
from models.word_eval import WordEmbeddingEvaluator 

model_name = 'word2vec'

if model_name == 'word2vec': 
    model = WordEmbeddingEvaluator(
        vecs_txt_fname= '/notebooks/embedding/data/word-embeddings/\
    word2vec/word2vec', method='word2vec', dim=100, tokenizer_name='mecab')
elif model_name == 'fasttext': 
    model = WordEmbeddingEvaluator(
    vecs_txt_fname='/notebooks/embedding/data/word-embeddings/\
        fasttext/fasttext.vec',
    vecs_bin_fname='/notebooks/embedding/data/word-embeddings/\
        fasttext/fasttext.bin',
    method='fasttext', dim=100, tokenizer_name='mecab')
elif model_name == 'glove': 
    model = WordEmbeddingEvaluator(
        vecs_txt_fname= '/notebooks/embedding/data/word-embeddings/\
    glove/glove.txt', method='glove', dim=100, tokenizer_name='mecab')
elif model_name == 'swivel':
    model = WordEmbeddingEvaluator(
        vecs_txt_fname= '/notebooks/embedding/data/word-embeddings/\
    swivel/row_embeddings.tsv', method='swivel', dim=100, tokenizer_name='mecab')
else: 
    print('model name error!')

