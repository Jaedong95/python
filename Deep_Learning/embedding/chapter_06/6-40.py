'''
BERT 임베딩 시각화 (2)
BERT 트랜스포머 블록별 셀프 어텐션 스코어를 모두 합해 문장 내 각 토큰 사이에
얼마나 강한 유대 관계가 있는지를 시각화 
'''
model.visualize_self_attention_scores('이 영화 엄청 재미있네요')
