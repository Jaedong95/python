'''
BERTTuner 클래스 (1)  - 선언부 
BERT 모델 파인 튜닝을 위한 각종 하이퍼파라미터 값들을 정하고, 코드 6-29의 
파인튜닝 네트워크 텐서 그래프를 그림 
'''
class BERTTuner(Tuner):
    def __init__(self, train_corpus_fname, test_corpus_fname, vocab_fname,
                 pretrain_model_fname, bertconfig_fname, model_save_path,
                 max_seq_length=128, warmup_proportion=0.1,
                 batch_size=32, learning_rate=2e-5, num_labels=2):
        # Load a corpus.
        super().__init__(train_corpus_fname=train_corpus_fname,
                         tokenized_train_corpus_fname=train_corpus_fname + ".bert-tokenized",
                         test_corpus_fname=test_corpus_fname, batch_size=batch_size,
                         tokenized_test_corpus_fname=test_corpus_fname + ".bert-tokenized",
                         model_name="bert", vocab_fname=vocab_fname, model_save_path=model_save_path)
        # configurations
        config = BertConfig.from_json_file(bertconfig_fname)
        self.pretrain_model_fname = pretrain_model_fname
        self.max_seq_length = max_seq_length
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.num_labels = 2 # positive, negative
        self.PAD_INDEX = 0
        self.CLS_TOKEN = "[CLS]"
        self.SEP_TOKEN = "[SEP]"
        self.num_train_steps = (int((len(self.train_data) - 1) / self.batch_size) + 1) * self.num_epochs
        self.num_warmup_steps = int(self.num_train_steps * warmup_proportion)
        self.eval_every = int(self.num_train_steps / self.num_epochs)  # epoch마다 평가
        self.training = tf.placeholder(tf.bool)
        # build train graph
        self.input_ids, self.input_mask, self.segment_ids, self.label_ids, self.logits, self.loss = make_bert_graph(config,
                                                                                                                    max_seq_length,
                                                                                                                    self.dropout_keep_prob_rate,
                                                                                                                    num_labels, tune=True)