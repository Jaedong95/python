'''
데이터 확보에서 전처리한 네이버 영화 리뷰 말뭉치를 활용해 soynlp 띄어쓰기 모듈 학습 
'''
from soyspacing.countbase import CountSpace 

corpus_fname = '/notebooks/embedding/data/processed/processed_ratings.txt'
model_fname = '/notebooks/embedding/data/processed/space-correct.model' 

model = CountSpace()   # 띄어쓰기 모듈 생성 
model.train(corpus_fname)   # 모델 학습 
model.save_model(model_fname, json_format=False)   # 모델 저장 