'''
새로운 문서의 토픽 확인 
'''
# LDA 모델에 넣어 토픽을 추론해 가장 높은 확률 값을 지니는 토픽 ID & 확률 리턴 
# 해당 문서의 토픽 분포 가운데 0.5를 넘는 지배적인 토픽이 존재하지 않는 경우 there is no dominant topic message return
model.show_new_document_topic(['너무 사랑스러운 영화', '인생을 말하는 영화'])