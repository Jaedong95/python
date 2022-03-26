'''
단어-문맥 행렬을 활용한 LSA 
'''
from sklearn.decomposition import TruncatedSVD 
from soynlp.vectorizer import sent_to_word_contexts_matrix 

corpus_fname = '/notebooks/embedding/data/tokenized/for-lsa-mecab.txt'
corpus = [sent.replace('\n', '').strip() for sent in \
    open(corpus_fname, 'r').readlines()]

# 단어-문맥 행렬 구축 
input_matrix, idx2vocab = sent_to_word_contexts_matrix(
    corpus, 
    windows=3,   # 타깃 단어 앞뒤 3개 단어를 문맥으로 고려 
    min_tf=10, 
    # False -> 윈도우 내에 포함된 모든 문맥 단어들의 동시 등장 점수 = 1
    dynamic_weight=True,   
    verbose=True
)

cooc_svd = TruncatedSVD(n_components=100)
cooc_vecs = cooc_svd.fit_transform(input_matrix)