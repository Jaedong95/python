'''
ELMo의 문장 임베딩 추출 
'''

# get_sentence_vector 함수는 문장을 입력하면 형태소 분석 결과 + 토큰 시퀀스의 마지막 단어에 해당하는 벡터 반환
model.get_sentence_vector("이 영화 엄청 재미있네요") # ELMo의 문장 임베딩 추출