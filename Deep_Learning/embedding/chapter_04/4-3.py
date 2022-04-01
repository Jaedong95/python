''''
Word2Vec Skip-gram 모델 학습 
'''
corpus_fname = '/notebooks/embedding/data/tokenized/corpus_mecab.txt'
model_fname = '/notebooks/embedding/data/data/word-embeddings/word2vec/word2vec' 

from gensim.models import Word2Vec 

corpus = [sent.strip().split(' ') for sent in open(corpus_fname, 'r').readlines()] 
 # size: Word2Vec 임베딩의 차원 수,  sg=1  -> Skip-gram, 0  -> CBOW 모델로 학습 
model = Word2Vec(corpus, size=100, workers=4, sg=1) 
model.save(model_fname)   # 모델 저장 asd