'''
LDA 학습 및 결과 확인 
'''
from gensim.models import ldamulticore 

LDA = ldamulticore.LdaMulticore(corpus, id2word=dictionary,
                                num_topics = 30,   # 토픽 수  
                                workers=4)  

# get_document_topics: 학습이 끝난 DLA 모델로부터 각 문서별 토픽 분포 리턴 
all_topics = LDA.get_document_topics(corpus, \
    minimum_probability=0.5,   # 0.5 미만의 토픽 분포 무시 
    per_word_topics=False)  