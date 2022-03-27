'''
WordEmbeddingTuner 클래스 (4)  - 옵티마이저 등 정의 
이 함수를 호출하면 파인 튜닝 네트워크의 학습이 시작됨 
'''
def tune(self):
    global_step = tf.train.get_or_create_global_step()   # global step을 불러옴 
    optimizer = tf.train.AdamOptimizer(learning_rate=self.lr)   # Adam Optimizer 생성 
    grads_and_vars = optimizer.compute_gradients(self.loss)   # gradient 계산 
    train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)
    output_feed = [train_op, global_step, self.logits, self.loss]
    saver = tf.train.Saver(max_to_keep=1)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())   # 글로벌 변수 초기화 
    sess.run(self.embed_init, feed_dict={self.embedding_placeholder: self.embeddings})
    self.train(sess, saver, global_step, output_feed)   # 모델 학습 