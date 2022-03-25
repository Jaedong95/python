'''
전처리를 수행한 한국어 위키백과 데이터를 가지고 BPE 알고리즘으로 
어휘집합 (vocabulary) 생성 
'''
import sentencepiece as spm 

train = """--input=/notebooks/embedding/data/processed/processed_wiki_ko.txt \
    --model_prefix=sentpiece \ 
    --vocab_size=32000 \ 
    --model_type=bpe --character_coverage=0.9995"""

spm.SentencePieceTrainer.Train(train)   # SentencePiece 모델 학습 

# 센텐스피스 패키지 학습 결과를 BERT에 사용할 수 있는 어휘 집합으로 쓸 수 있게 
# 하기 위해서는 일부 후처리가 필요함 
