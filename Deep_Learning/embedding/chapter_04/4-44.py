'''
CBoWModel(3)  - 가중 임베딩 만들기 
코드 4-43에서 확인한 임베딩 말뭉치 통계량을 바탕으로 가중 임베딩 생성 
모든 단어 벡터 각각에 수식 4-29를 적용해 해당 단어 등장 확률을 반영한 가중치를 곱함 
''' 
def load_or_construct_weighted_embedding(self, embedding_fname, embedding_method,\
     embedding_corpus_fname, a=0.0001):

    dictionary = {}
    if os.path.exists(embedding_fname + "-weighted"):   # 가중 임베딩 저장 경로
        # load weighted word embeddings
        with open(embedding_fname + "-weighted", "r") as f2:
            for line in f2:
                word, weighted_vector = line.strip().split("\u241E")
                weighted_vector = [float(el) for el in weighted_vector.split()]
                dictionary[word] = weighted_vector
    else:
        # load pretrained word embeddings
        words, vecs = self.load_word_embeddings(embedding_fname, embedding_method)
        # compute word frequency
        words_count, total_word_count = self.compute_word_frequency(embedding_corpus_fname)
        # construct weighted word embeddings
        with open(embedding_fname + "-weighted", "w") as f3:
            for word, vec in zip(words, vecs):
                if word in words_count.keys():
                    word_prob = words_count[word] / total_word_count
                else:
                    word_prob = 0.0
                weighted_vector = (a / (word_prob + a)) * np.asarray(vec)
                dictionary[word] = weighted_vector
                f3.writelines(word + "\u241E" + " ".join([str(el) for el in weighted_vector]) + "\n")
    return dictionary