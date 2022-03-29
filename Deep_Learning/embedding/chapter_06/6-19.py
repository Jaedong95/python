'''
ELMoTuner 클래스 (1)  - 선언부 
ELMo 파인 튜닝 네트워크를 학습하는 역할 수행 
부모 클래스 Tuner + 입력 단어들을 ID로 변환하는 역할을 하는 Batcher 정의
+ ELMo 파인 튜닝 네트워크의 텐서 그래프를 그림  
'''
class ELMoTuner(Tuner):
    def __init__(self, train_corpus_fname, test_corpus_fname,
                 vocab_fname, options_fname, pretrain_model_fname,
                 model_save_path, max_characters_per_token=30,
                 batch_size=32, num_labels=2):
        # Load a corpus.
        super().__init__(train_corpus_fname=train_corpus_fname,
                         tokenized_train_corpus_fname=train_corpus_fname + ".elmo-tokenized",
                         test_corpus_fname=test_corpus_fname,
                         tokenized_test_corpus_fname=test_corpus_fname + ".elmo-tokenized",
                         model_name="elmo", vocab_fname=vocab_fname,
                         model_save_path=model_save_path, batch_size=batch_size)
        # configurations
        self.options_fname = options_fname
        self.pretrain_model_fname = pretrain_model_fname
        self.max_characters_per_token = max_characters_per_token
        self.num_labels = 2 # positive, negative
        self.num_train_steps = (int((len(self.train_data) - 1) / self.batch_size) + 1) * self.num_epochs
        self.eval_every = int(self.num_train_steps / self.num_epochs)  # epoch마다 평가
        # Create a Batcher to map text to character ids.
        # lm_vocab_file = ELMo는 token vocab이 없어도 on-the-fly로 입력 id들을 만들 수 있다
        # 하지만 자주 나오는 char sequence, 즉 vocab을 미리 id로 만들어 놓으면 좀 더 빠른 학습이 가능
        # max_token_length = the maximum number of characters in each token
        self.batcher = Batcher(lm_vocab_file=vocab_fname, max_token_length=self.max_characters_per_token)
        self.training = tf.placeholder(tf.bool)
        # build train graph
        self.ids_placeholder, self.labels_placeholder, self.dropout_keep_prob, self.logits, self.loss = make_elmo_graph(options_fname,
                                                                                                                        pretrain_model_fname,
                                                                                                                        max_characters_per_token,
                                                                                                                        num_labels, tune=True)
                                                                                                                        
                                                                                                                        