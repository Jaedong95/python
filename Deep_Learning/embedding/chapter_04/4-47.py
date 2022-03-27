'''
CBoWModel(6)  - 문장 1개 예측 
'''
def predict(self, sentence):
    tokens = self.tokenizer.morphs(sentence)   # 형태소 분석 수행 
    sentence_vector = self.get_sentence_vector(tokens)   # 문장 임베딩으로 변환 
    # 벡터 내적을 통해 코사인 유사도 도출 
    scores = np.dot(self.model["vectors"], sentence_vector)   
    pred = self.model["labels"][np.argmax(scores)]   # 가장 큰 유사도 가진 문장의 인덱스 추출 
    return pred