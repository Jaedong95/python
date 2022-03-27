'''
Tuner 클래스 (1)  - 선언 
'''
class Tuner(object):
    def __init__(self, train_corpus_fname=None, tokenized_train_corpus_fname=None,
                 test_corpus_fname=None, tokenized_test_corpus_fname=None,
                 model_name="bert", model_save_path=None, vocab_fname=None, eval_every=1000,
                 batch_size=32, num_epochs=10, dropout_keep_prob_rate=0.9, model_ckpt_path=None,
                 sp_model_path=None):
        # configurations
        tf.logging.set_verbosity(tf.logging.INFO)
        self.model_name = model_name
        self.eval_every = eval_every
        self.model_ckpt_path = model_ckpt_path
        self.model_save_path = model_save_path
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.dropout_keep_prob_rate = dropout_keep_prob_rate
        self.best_valid_score = 0.0
        if not os.path.exists(model_save_path):
            os.mkdir(model_save_path)
        # define tokenizer
        if self.model_name == "bert":
            self.tokenizer = FullTokenizer(vocab_file=vocab_fname, do_lower_case=False)
        elif self.model_name == "xlnet":
            sp = spm.SentencePieceProcessor()
            sp.Load(sp_model_path)
            self.tokenizer = sp
        else:
            self.tokenizer = get_tokenizer("mecab")
        # load or tokenize corpus
        self.train_data, self.train_data_size = self.load_or_tokenize_corpus(\
            train_corpus_fname, tokenized_train_corpus_fname)
        self.test_data, self.test_data_size = self.load_or_tokenize_corpus(\
            test_corpus_fname, tokenized_test_corpus_fname)