'''
유사 문서 검색 
'''
from models.sent_eval import LSAEvaluator 

model = LSAEvaluator('data/sentence-embeddings/lsa-tfidf/lsa-tfidf.vecs')
# 0번째 문서 임베딩과 코사인 유사도가 가장 높은 문서 임베딩의 제목 리턴 
model.most_similar(doc_id=0)  
