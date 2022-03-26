'''
CBoWModel(7)  - Batch 단위 예측 
'''
def predict_by_batch(self, tokenized_sentences, labels):
    sentence_vectors, eval_score = [], 0
    # 테스트 문장 벡터 여러 개를 묶음 
    for tokens in tokenized_sentences:
        sentence_vectors.append(self.get_sentence_vector(tokens))

    scores = np.dot(self.model["vectors"], np.array(sentence_vectors).T)   # 내적 
    preds = np.argmax(scores, axis=0)
    for pred, label in zip(preds, labels):
        if self.model["labels"][pred] == label:
            eval_score += 1
    return preds, eval_score