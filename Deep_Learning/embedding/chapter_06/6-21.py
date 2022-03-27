'''
ELMoTuner 클래스 (3)  - 옵티마이저 등 정의 
ELMoTuner의 이 함수를 호출하면 ELMo 파인 튜닝 네트워크의 학습 수행 
'''
def tune(self):
    global_step = tf.train.get_or_create_global_step()
    optimizer = tf.train.AdamOptimizer(learning_rate=0.0001)
    grads_and_vars = optimizer.compute_gradients(self.loss)
    train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)
    output_feed = [train_op, global_step, self.logits, self.loss]
    saver = tf.train.Saver(max_to_keep=1)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    self.train(sess, saver, global_step, output_feed)