'''
Doc2Vec 평가 클래스 선언 
'''
from models.sent_eval import Doc2VecEvaluator 

model = Doc2VecEvaluator('/notebooks/embedding/data/\
    sentence-embeddings/doc2vec/doc2vec.model')