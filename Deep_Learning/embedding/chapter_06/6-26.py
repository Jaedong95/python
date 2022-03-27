'''
ELMo의 토큰별 임베딩 추출 
get_token_vector_sequence() 함수를 호출하면 형태소 분석 결과와 토큰별 ELMo 벡터들 반환 
'''
model.get_token_vector_sequence("이 영화 엄청 재미있네요") # ELMo의 토큰별 임베딩 추출