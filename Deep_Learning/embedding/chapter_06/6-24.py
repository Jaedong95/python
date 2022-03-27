'''
ELMoEmbeddingEvaluator 선언 
'''
from models.sent_eval import ELMoEmbeddingEvaluator

model = ELMoEmbeddingEvaluator(tune_model_fname="/notebooks/embedding/data/\
    sentence-embeddings/elmo/tune-ckpt",
    pretrain_model_fname="/notebooks/embedding/data/sentence-embeddings/\
    elmo/pretrain-ckpt/elmo.model",
    options_fname="/notebooks/embedding/data/sentence-embeddings/elmo/pretrain-ckpt/options.json",
    vocab_fname="/notebooks/embedding/data/sentence-embeddings/elmo/pretrain-ckpt/elmo-vocab.txt",
    max_characters_per_token=30,   # 토큰 하나당 최대 문자 길이 
    dimension=256,   # ELMo 임베딩의 차원 수 
    num_labels=2)   # ELMo를 파인튜닝할 때 분류 범주의 수 