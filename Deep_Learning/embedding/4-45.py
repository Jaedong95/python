'''
CBoWModel (4)  - 모델 학습 
형태소 분서기 완료된 리뷰에 코드 4-46에 정의된 get_sentece_vector를 적용해 문장 벡터 생성 
'''
def train_model(self, train_data_fname, model_fname):
    model = {"vectors": [], "labels": [], "sentences": []}
    train_data = self.load_or_tokenize_corpus(train_data_fname)
    with open(model_fname, "w") as f:
        # 학습 데이터 모든 문장에 대해 적용 
        for sentence, tokens, label in train_data:
            tokens = self.tokenizer.morphs(sentence)
            sentence_vector = self.get_sentence_vector(tokens)
            model["sentences"].append(sentence)
            model["vectors"].append(sentence_vector)
            model["labels"].append(label)
            str_vector = " ".join([str(el) for el in sentence_vector])
            # 문장 + 형태소 분석된 문장 (token) + 극성 레이블 묶어 저장 
            f.writelines(sentence + "\u241E" + " ".join(tokens) + "\u241E" \
                + str_vector + "\u241E" + label + "\n")
    return model