'''
BERT의 토큰별 임베딩 추출 
get_token_vector_sequence() 함수를 호출하면 형태소 분석 결과와 토큰별 ELMo 벡터들 반환 
BERT는 입력 과정에서 문장 시작과 끝을 알리는 스폐셜 토큰 [CLS], [SEP]를 앞뒤로 붙이기 
때문에 반환하는 토큰 벡터의 수는 (원래 토큰 수 + 2)개가 됨 
'''
model.get_token_vector_sequence("이 영화 엄청 재미있네요") # ELMo의 토큰별 임베딩 추출