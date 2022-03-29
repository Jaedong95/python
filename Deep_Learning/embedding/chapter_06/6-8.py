'''
WordEmbeddingTuner 클래스 (1)  - 선언부 
6.2절에서 정의한 Tuner를 상속받음 
학습 데이터 로딩, 배치 생성, 학습 및 평가 함수등을 따로 정의할 필요 x 
단어 임베딩 모델에 특화한 함수들만 추가적으로 정의해 줌 
'''
class WordEmbeddingTuner(Tuner):
    def __init__(self, train_corpus_fname, test_corpus_fname,
                 model_save_path, embedding_name, embedding_fname=None,
                 embedding_size=100, batch_size=128, learning_rate=0.0001, num_labels=2):
        # Corpus 로드 
        super().__init__(train_corpus_fname=train_corpus_fname,
                         tokenized_train_corpus_fname=train_corpus_fname + ".word-embedding-tokenized",
                         test_corpus_fname=test_corpus_fname, batch_size=batch_size,
                         tokenized_test_corpus_fname=test_corpus_fname + ".word-embedding-tokenized",
                         model_name=embedding_name, model_save_path=model_save_path)
        self.lr = learning_rate
        self.embedding_size = embedding_size
        # 단어 임베딩 로드하기 
        self.embeddings, self.vocab = self.load_embeddings(embedding_name, embedding_fname)
        self.unk_idx = len(self.vocab)
        self.pad_idx = len(self.vocab) + 1
        # 파인 튜닝 그래프 구축 
        self.ids_placeholder, self.input_lengths, self.labels_placeholder, \
        self.dropout_keep_prob, self.embedding_placeholder, self.embed_init, \
        # make_word_embedding_graph 호출 시 tune=True로 설정하면 파인 튜닝 네트워크 학습용
        self.logits, self.loss = make_word_embedding_graph(num_labels, len(self.vocab) + 2, self.embedding_size, tune=True)
    
    # tune 함수 오버라이드 
    def tune(self):
        global_step = tf.train.get_or_create_global_step()
        optimizer = tf.train.AdamOptimizer(learning_rate=self.lr)
        grads_and_vars = optimizer.compute_gradients(self.loss)
        train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)
        output_feed = [train_op, global_step, self.logits, self.loss]
        saver = tf.train.Saver(max_to_keep=1)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        sess.run(self.embed_init, feed_dict={self.embedding_placeholder: self.embeddings})
        self.train(sess, saver, global_step, output_feed)