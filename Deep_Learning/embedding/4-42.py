'''
CBoWModel(1)  - 선언부 
해당 클래스를 호출하면 각종 설정 정보를 저장해두고 형태소 분석기를 읽어들임 
'''
class CBoWModel(object):
    def __init__(self, train_fname, embedding_fname, model_fname, embedding_corpus_fname,
                 embedding_method="fasttext", is_weighted=True, average=False, dim=100,
                  tokenizer_name="mecab"):
        # configurations
        make_save_path(model_fname)
        self.dim = dim
        self.average = average
        if is_weighted:
            model_full_fname = model_fname + "-weighted"
        else:
            model_full_fname = model_fname + "-original"
        self.tokenizer = get_tokenizer(tokenizer_name)
        if is_weighted:
            # ready for weighted embeddings
            self.embeddings = self.load_or_construct_weighted_embedding(embedding_fname, embedding_method, embedding_corpus_fname)
            print("loading weighted embeddings, complete!")
        else:
            # ready for original embeddings
            words, vectors = self.load_word_embeddings(embedding_fname, embedding_method)
            self.embeddings = defaultdict(list)
            for word, vector in zip(words, vectors):
                self.embeddings[word] = vector
            print("loading original embeddings, complete!")
        if not os.path.exists(model_full_fname):
            print("train Continuous Bag of Words model")
            self.model = self.train_model(train_fname, model_full_fname)
        else:
            print("load Continuous Bag of Words model")
            self.model = self.load_model(model_full_fname)