'''
Doc2Vec 입력 클래스 
'''
from preprocess import get_tokenizer
from gensim.models.doc2vec import TaggedDocument

# Doc2VecInput 클래스는 Doc2Vec 클래스가 요구하는 입력 형태를 맞춰줌
class Doc2VecInput:
    def __init__(self, fname, tokenizer_name="mecab"):
        self.fname = fname
        self.tokenizer = get_tokenizer(tokenizer_name)

    def __iter__(self):
        with open(self.fname, encoding='utf-8') as f:
            for line in f:
                try:
                    sentence, movie_id = line.strip().split("\u241E")
                    tokens = self.tokenizer.morphs(sentence)
                    tagged_doc = TaggedDocument(words=tokens, tags=['MOVIE_%s' % movie_id])
                    yield tagged_doc
                except:
                    continue