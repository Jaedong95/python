'''
Doc2Vec 학습 
'''
from gensim.models import Doc2Vec 

corpus_fname = '/notebooks/embedding/data/processed/processed_review_movieid.txt'
output_fname = '/notebooks/embedding/data/sentence-embeddings/doc2vec/doc2vec.model'

corpus = Doc2VecInput(corpus_fname)

# dm: 어떤 Doc2Vec 모델을 사용할 지 결정, 1이면 PV-DM, 0이면 PV-DBOW 사용 
model = Doc2Vec(corpus, dm=1, vector_size=100)
model.save(output_fname)