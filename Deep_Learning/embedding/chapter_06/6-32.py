'''
BERTTuner 클래스 (3)  - 옵티마이저 등 정의 
BERT 모델은 프리트레인뿐만 아니라 파인 튜닝에서도 웜업 방식의 아담 옵티마이저 사용 
BRERTuner의 이 함수를 호출하면 BERT 파인 튜닝 네트워크의 학습이 시작됨 
'''
def tune(self):
    '''
    global_step, optimizer, session 등을 정의 
    '''
    global_step = tf.train.get_or_create_global_step()
    tf.logging.info("num_train_steps: " + str(self.num_train_steps))
    tf.logging.info("num_warmup_steps: " + str(self.num_warmup_steps))
    train_op = create_optimizer(self.loss, self.learning_rate, self.num_train_steps, self.num_warmup_steps, use_tpu=False)
    output_feed = [train_op, global_step, self.logits, self.loss]
    restore_vars = [v for v in tf.trainable_variables() if "bert" in v.name]
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    tf.train.Saver(restore_vars).restore(sess, self.pretrain_model_fname)
    saver = tf.train.Saver(max_to_keep=1)
    self.train(sess, saver, global_step, output_feed)

