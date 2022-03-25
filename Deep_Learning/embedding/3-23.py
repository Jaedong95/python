'''
코드 3-22에서 학습한 단어 점수표를 활용해 '애비는 종이었다'라는 
문장 하나를 형태소 분석 
'''
import math 
from soynlp.word import WordExtractor 
from soynlp.tokenizer import LTokenizer 

model_fname = '/notebooks/embedding/data/processed/soyword.model' 

# WordExtractor 클래스 생성 
word_extractor = WordExtractor(min_frequency=100, min_cohension_forward=0.05, \
    min_right_branching_entropy=0.0 )
word_extractor.load(model_fname)   # 이전에 학습한 모델 로드
scores = word_extractor.word_scores()   # 단어 점수표 생성 
scores = {key: (scores[key].cohension_forward * \
    math.exp(scores[key].right_branching_entroyp)) for key in scores.keys()}
