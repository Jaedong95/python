'''
CBoWModel (5)  - 문장 임베딩 만들기 
'''
def get_sentence_vector(self, tokens):
    vector = np.zeros(self.dim)
    for token in tokens:
        if token in self.embeddings.keys():
            vector += self.embeddings[token]
    if not self.average:
        vector /= len(tokens)
    # 크기가 1인 단위 벡터 형태로 바꿔 리턴 
    vector_norm = np.linalg.norm(vector)   # 벡터 정규화 
    if vector_norm != 0:
        unit_vector = vector / vector_norm
    else:
        unit_vector = np.zeros(self.dim)
    return unit_vector
