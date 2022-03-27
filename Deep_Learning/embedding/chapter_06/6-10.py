'''
WordEmbeddingTuner 클래스 (3)  - 입력값 생성 함수 
부모 클래스인 Tuner의 배치 생성 함수 get_batch가 배치를 만들 때 이 함수 호출
'''
def make_input(self, sentences, labels, is_training):
    '''
    입력값 생성 
    '''
    input_ids, lengths = [], []
    max_token_length = self.get_max_token_length_this_batch(sentences)
    
    # 토큰들을 어휘 집합에 해당하는 ID들로 변환
    for tokens in sentences:
        token_ids = []
        tokens_length = len(tokens)
        for token in tokens:
            if token in self.vocab:
                token_ids.append(self.vocab[token])
            else:   # 어휘 집합에 없는 토큰: [UNK] 토큰 ID로 바꿔줌 
                token_ids.append(self.unk_idx)

        # 배치 데이터를 생성할 문장들의 토큰 수 기준 최대 길이를 확인하고, 
        # 이보다 짧으면 [PAD]에 해당하는 ID(len(self.vocab) + 1)를 붙여 해당 길이로 맞춰줌
        if len(tokens) < max_token_length:
            token_ids.extend(
                [self.pad_idx] * (max_token_length - tokens_length))
        input_ids.append(token_ids)
        lengths.append(len(token_ids))
    if is_training:   # 학습시에는 Dropout을 수행 
        input_feed = {
            self.ids_placeholder: np.array(input_ids),
            self.input_lengths: np.array(lengths),
            self.labels_placeholder: np.array(labels),
            self.dropout_keep_prob: 0.9
        }
    else:   # 그외에는 Dropout을 하지 x (Dropout_keep_prob=1.0)
        input_feed = {
            self.ids_placeholder: np.array(input_ids),
            self.input_lengths: np.array(lengths),
            self.labels_placeholder: np.array(labels),
            self.dropout_keep_prob: 1.0
        }
        input_feed = [input_feed, labels]
    return input_feed