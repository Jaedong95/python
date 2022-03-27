'''
Tuner 클래스 (3)  - 배치 함수 
사용자가 정한 에폭 수만큼 배치 데이터를 반복 생성 
매 에폭마다 전체 학습 데이터를 랜덤 셔플 수행 
데이터: 문장 (영화 리뷰) + 레이블 (긍정 or 부정) 쌍으로 구성됨 
배치: 이미 셔플한 말뭉치에서 batch_size만큼 슬라이딩하며 순서대로 생성됨

네이버 영화 리뷰의 테스트 데이터는 GPU가 한번에 계산할 수 있는 batch_size보다 큼 
-> 평가 때에도 배치 단위로 모델에 피드해 줘야 함 
'''
def get_batch(self, data, num_epochs, is_training=True):
    '''
    
    '''
    if is_training:
        data_size = self.train_data_size
    else:
        data_size = self.test_data_size
    num_batches_per_epoch = int((data_size - 1) / self.batch_size)
    if is_training:
        tf.logging.info("num_batches_per_epoch : " + str(num_batches_per_epoch))
    for epoch in range(num_epochs):
        idx = random.sample(range(data_size), data_size)
        data = np.array(data)[idx]
        for batch_num in range(num_batches_per_epoch):
            batch_sentences = []
            batch_labels = []
            start_index = batch_num * self.batch_size
            end_index = (batch_num + 1) * self.batch_size
            features = data[start_index:end_index]
            for feature in features:
                sentence, label = feature
                batch_sentences.append(sentence)
                batch_labels.append(int(label))
            yield self.make_input(batch_sentences, batch_labels, is_training)