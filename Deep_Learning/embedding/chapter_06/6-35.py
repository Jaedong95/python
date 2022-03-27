'''
BERTEmbeddingEvaluator 선언 
'''
from models.sent_eval import BERTEmbeddingEvaluator 

model = BERTEmbeddingEvaluator(
    model_fname='/notebooks/embedding/data/sentence-embeddings/bert/tune-ckpt',
    bertconfig_fname='/notebooks/embedding/data/sentence-embeddings/bert/\
        pretrain-ckpt/bert_config.json',
    vocab_fname='/notebooks/embedding/data/sentence-embeddings/bert/\
        pretrain-ckpt/vocab.txt', 
    max_seq_length=32,   # 입력 문장의 토큰 수 기준 최대 길이 
    dimension=768,  # BERT 임베딩의 차원 수 
    num_labels=2)   # 파인 튜닝 데이터셋의 범주 수 
