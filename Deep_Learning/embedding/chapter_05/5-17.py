'''
Doc2Vec 학습 데이터에 포함된 영화를 30개 랜덤 추출해 해당 벡터를 뽑고, 
그 벡터들을 시각화 
'''
model.visualize_movies(type='between')
model.visualize_movies(type='tsne')
