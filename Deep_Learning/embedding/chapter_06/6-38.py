'''
BERT의 문장 임베딩 추출 
문장을 입력하면 워드피스의 형태소 분석 결과 + BERT 모델의 pooled_output 벡터 반환 
pooled_output: 문장 시작을 알리는 첫 번째 토큰 [CLS]에 해당하는 벡터에 선형변환을 
               한 차례한 뒤 하이퍼볼릭탄젠트를 적용한 결과
'''
model.get_sentence_vector("이 영화 엄청 재미있네요") # ELMo의 문장 임베딩 추출