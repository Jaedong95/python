# Tuner클래스(5)  - 평가 함수 
def validation(self, sess, saver, global_step):
    '''
    테스트 데이터 전체를 1회(num_epochs=1) 평가 
    모델이 테스트 데이터를 보고 학습하면 안되기 때문에, output_feed 부분에서 optimizer 제외 
    로짓 벡터의 최댓값이 어느 레이블에 해당하는지를 조사해 예측 레이블 생성 
    예측 레이블이 정답과 일치하면 점수 (valid_pred) + 1 
    이 점수가 이전 평가 점수보다 높으면 모델의 체크포인트를 정해진 경로에 저장
    '''
    valid_loss, valid_pred, valid_num_data = 0, 0, 0
    output_feed = [self.logits, self.loss]
    test_batches = self.get_batch(self.test_data, num_epochs=1, is_training=False)
    for current_input_feed, current_labels in test_batches:
        current_logits, current_loss = sess.run(output_feed, current_input_feed)
        current_preds = np.argmax(current_logits, axis=-1)
        valid_loss += current_loss
        valid_num_data += len(current_labels)
        for pred, label in zip(current_preds, current_labels):
            if pred == label:
                valid_pred += 1
    valid_score = valid_pred / valid_num_data
    tf.logging.info("valid loss %.4f valid score %.4f" %
                    (valid_loss, valid_score))
    if valid_score > self.best_valid_score:
        self.best_valid_score = valid_score
        path = self.model_save_path + "/" + str(valid_score)
        saver.save(sess, path, global_step=global_step)