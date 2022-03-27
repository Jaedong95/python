'''
WordEmbedding Tuner 클래스 (2)  - 단어 임베딩 로드 함수 
'''
def get_truncated_normal(self, mean=0, sd=1, low=-1, upp=1):
    '''
    이미 학습된 단어 임베딩 행렬에 추가로 스페셜 토큰 [UNK]에 해당하는 벡터 추가 
    배치를 생성할 때 길이가 짧은 문서에 덧붙여주는 스페셜 토큰 [PAD]에 해당하는 벡터 추가 
    '''
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
        

def load_embeddings(self, embedding_name, embedding_fname):
    '''
    Word2Vec, GloVe, FastText, Swivel 등 이미 학습된 단어 임베딩 행렬을 
    읽어들이는 역할 수행 
    '''
    random_generator = self.get_truncated_normal()
    if embedding_name in ["fasttext", "glove", "swivel"]:
        embeddings, words = [], []
        with open(embedding_fname, 'r') as f:
            if embedding_name == "fasttext":
                next(f) # skip head line
            for line in f:
                if embedding_name == "swivel":
                    splitedLine = line.strip().split("\t")
                else:
                    splitedLine = line.strip().split()
                word = splitedLine[0]
                embedding = [float(el) for el in splitedLine[1:]]
                words.append(word)
                embeddings.append(embedding)
        embeddings = np.array(embeddings)
        vocab = {word:idx for idx, word in enumerate(words)}
    elif embedding_name == "word2vec":
        model = Word2Vec.load(embedding_fname)
        embeddings = model.wv.vectors
        vocab = {word:idx for idx, word in enumerate(model.wv.index2word)}
    else:
        words_count = defaultdict(int)
        for tokens, _ in self.train_data:
            for token in tokens:
                words_count[token] += 1
        sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:50000]
        words = [word for word, _ in sorted_words]
        vocab = {word:idx for idx, word in enumerate(words)}
        random_embeddings = random_generator.rvs(len(vocab) * self.embedding_size)
        embeddings = random_embeddings.reshape(len(vocab), self.embedding_size)
    # for UNK, PAD token
    added_embeddings = random_generator.rvs(self.embedding_size * 2)
    embeddings = np.append(embeddings, added_embeddings.reshape(2, self.embedding_size), axis=0)
    return embeddings, vocab