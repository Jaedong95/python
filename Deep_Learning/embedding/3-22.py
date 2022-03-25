'''
soynlp의 단어점수 학습 
WordExtractor 클래스의 입력 타입: 하나의 요소가 문서인 리스트 
'''
from soynlp.word import WordExtractor 

corpus_fname = '/notebooks/embedding/data/processed/processed_ratings.txt'
model_fname = '/notebooks/embedding/data/processed/soyword.model' 

# corpus file을 읽어 공백을 제거하고, 문장 단위로 리스트에 저장 
sentences = [sent.strip() for sent in open(corpus_fname, 'r').readlines()]

# WordExtractor 클래스 생성 
word_extractor = WordExtractor(min_frequency=100, min_cohension_forward=0.05, \
    min_right_branching_entropy=0.0 )
word_extractor.train(sentences)   # 단어점수 학습 
word_extractor.save(model_fname)   # 학습한 모델(단어 점수표) 저장 

# soynlp의 LTokenizer 클래스는 입력 문장의 오니쪽부터 문자 단위로 슬라이딩해가며 
# 단어 점수가 높은 문자열을 우선으로 형태소로 취급해 분리함 
# 띄어쓰기가 되어 있으면 해당 어절을 단어로 인식