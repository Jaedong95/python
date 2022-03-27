'''
ELMo 임베딩 시각화 
'''
sentences = ['이 영화 엄청 재미있네요', '이 영화 엄청 재미없네요', ...]
model.visualize_sentences(sentences)

# 입력 문장을 문장 임베딩으로 바꾼 후 벡터 간 코사인 유사도를 계산 후 Boekh로 시각화                  
model.visualize_between_senteces(sentences)