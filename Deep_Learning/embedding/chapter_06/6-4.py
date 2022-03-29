'''
Tuner 클래스 (4)  - 학습 함수 
'''
def train(self, sess, saver, global_step, output_feed):
    '''
    배치 데이터를 모델에 반복적으로 피드해 모델 학습 
    사용자가 정한 스텝 수를 만족하면 모델을 평가하기 위해 validation 함수 (6-5.py)호출 
    '''
    train_batches = self.get_batch(self.train_data, num_epochs=self.num_epochs, is_training=True)
    checkpoint_loss = 0.0
    for current_input_feed in train_batches:    # 학습셋의 배치 크기 단위로 
        _, _, _, current_loss = sess.run(output_feed, current_input_feed)   # 모델 학습 
        checkpoint_loss += current_loss   # 체크포인트 loss 계산 
        if global_step.eval(sess) % self.eval_every == 0:
            tf.logging.info("global step %d train loss %.4f" %
                            (global_step.eval(sess), checkpoint_loss / self.eval_every))
            checkpoint_loss = 0.0
            self.validation(sess, saver, global_step)