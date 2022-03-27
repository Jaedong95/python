'''
BERTTuner 클래스 (2)  - 입력값 생성함수 
'''
def make_input(self, sentences, labels, is_training):
    '''
    BERT 모델의 프리트레인과 달리 파인 튜닝 과정에서는 입력 문장이 A, B 두 개가 
    아닌 하나뿐이라고 가정
    '''
    collated_batch = {'sequences': [], 'segments': [], 'masks': []}
    for tokens in sentences:
        # 사용자가 정한 길이로 자름
        tokens = tokens[:(self.max_seq_length - 2)]
        # 문장들 앞뒤에 [CLS], [SEP] 토큰 붙임 
        token_sequence = [self.CLS_TOKEN] + tokens + [self.SEP_TOKEN]
        segment = [0] * len(token_sequence)
        # ID로 변환 
        sequence = self.tokenizer.convert_tokens_to_ids(token_sequence)
        current_length = len(sequence)
        padding_length = self.max_seq_length - current_length
        collated_batch['sequences'].append(sequence + [self.PAD_INDEX] * padding_length)
        collated_batch['segments'].append(segment + [self.PAD_INDEX] * padding_length)
        collated_batch['masks'].append([1] * current_length + [self.PAD_INDEX] * padding_length)
    if is_training:
        input_feed = {
            self.training: is_training,
            self.input_ids: np.array(collated_batch['sequences']),
            # segment: token_sequence만큼의 길이를 가진 영 벡터 
            self.segment_ids: np.array(collated_batch['segments']),
            # mask: 요소 값이 모두 1이고 token_sequence 길이만큼의 차원수를 가진 벡터 
            self.input_mask: np.array(collated_batch['masks']),
            self.label_ids: np.array(labels)
        }
    else:
        input_feed_ = {
            self.training: is_training,
            self.input_ids: np.array(collated_batch['sequences']),
            self.segment_ids: np.array(collated_batch['segments']),
            self.input_mask: np.array(collated_batch['masks']),
            self.label_ids: np.array(labels)
        }
        input_feed = [input_feed_, labels]
    return input_feed