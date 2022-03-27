'''
Tuner 클래스 (2)  - 말뭉치 로드 및 형태소 분석 
tokenized_corpus_fname 경로에 데이터가 존재하면 해당 경로의 데이터를 읽고, 
그렇지 않으면 corpus_fname 경로의 데이터를 읽어서 형태소 분석 수행 
'''
def load_or_tokenize_corpus(self, corpus_fname, tokenized_corpus_fname):
    data_set = []
    if os.path.exists(tokenized_corpus_fname):
        tf.logging.info("load tokenized corpus : " + tokenized_corpus_fname)
        with open(tokenized_corpus_fname, 'r') as f1:
            for line in f1:
                tokens, label = line.strip().split("\u241E")
                if len(tokens) > 0:
                    data_set.append([tokens.split(" "), int(label)])
    else:
        tf.logging.info("tokenize corpus : " + corpus_fname + " > " + tokenized_corpus_fname)
        with open(corpus_fname, 'r') as f2:
            next(f2)  # skip head line
            for line in f2:
                sentence, label = line.strip().split("\u241E")
                if self.model_name == "bert":
                    tokens = self.tokenizer.tokenize(sentence)
                elif self.model_name == "xlnet":
                    normalized_sentence = preprocess_text(sentence, lower=False)
                    tokens = encode_pieces(self.tokenizer, normalized_sentence, \
                        return_unicode=False, sample=False)
                else:
                    tokens = self.tokenizer.morphs(sentence)
                    tokens = post_processing(tokens)
                if int(label) > 0.5:
                    int_label = 1
                else:
                    int_label = 0
                data_set.append([tokens, int_label])
        with open(tokenized_corpus_fname, 'w') as f3:
            for tokens, label in data_set:
                f3.writelines(' '.join(tokens) + "\u241E" + str(label) + "\n")
    return data_set, len(data_set)