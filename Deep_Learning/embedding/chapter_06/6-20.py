'''
ELMoTuner 클래스 (2)  - 입력값 생성함수 
'''
def make_input(self, sentences, labels, is_training):
    '''
    입력값 생성 
    '''
    # 배치 문장들에 batcher.batch_sentences() 적용해 유니코드 ID들로 변환 
    current_input = self.batcher.batch_sentences(sentences)
    current_output = np.array(labels)
    if is_training:
        input_feed = {
            self.ids_placeholder: current_input,
            self.labels_placeholder: current_output,
            self.dropout_keep_prob: self.dropout_keep_prob_rate,
            self.training: True
        }
    else:
        input_feed_ = {
            self.ids_placeholder: current_input,
            self.labels_placeholder: current_output,
            self.dropout_keep_prob: 1.0,
            self.training: False
        }
        input_feed = [input_feed_, current_output]
    return input_feed