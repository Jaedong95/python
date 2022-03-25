'''
구글이 공개한 BERT 모델 코드에는 BPE로 학습한 어휘 집합으로 토큰을 
분리하는 클래스 (FullTokenizer)가 포함되어 있음, 학습한 어휘 집합으로 토큰 분리 
'''

from models.bert.tokenization import FullTokenizer 

vocab_fname = '/notebooks/embedding/data/processed/bert.vocab'   # 어휘 집합 
tokenizer = FullTokenizer(vocab_file=vocab_fname, do_lower_case=False)   # 토크나이저 생성 

tokenizer.tokenize('집에좀 가자')   # 토큰 분리 