'''
파인 튜닝 BERT 모델의 예측 
predict() 함수 실행 시 모델은 [해당 문장이 부정일 확률, 해당 문장이 긍정일 확률]의 
2차원 확률 벡터 반환 
'''
model.predict("이 영화 엄청 재미있네요")  # label 예측
model.predict("이 영화 엄청 재미없네요")
