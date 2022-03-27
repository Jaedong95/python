'''
TF-IDF 학습 결과 확인 
'''
id2vocab = {vectorizer.vocabulary_[token]:token \
    for token in vectorizer.vocabulary_.keys()}

# curr_doc: 말뭉치 첫 번째 문서의 TF-IDF 벡터 
curr_doc, result = input_matrix[0], [] 

# curr_doc에서 TF-IDF 값이 0이 아닌 요소들을 내림차순 정렬 
for idx, el in zip(curr_doc.indices, curr_doc.data):
    result.append((id2vocab[idx], el))

sorted(result, key=lambda x: x[1], reverse=True)