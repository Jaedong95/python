'''
CBoWModel (2)  - 임베딩 학습 말뭉치 내 단어별 빈도 확인 
임베딩 학습 말뭉치에 쓰인 모든 문장, 모든 단어의 빈도를 일일이 세어 둠 
입력되는 데이터는 이미 형태소 분석이 완료되었다고 가정 
'''
def compute_word_frequency(self, embedding_corpus_fname):
    total_count = 0
    words_count = defaultdict(int)
    with open(embedding_corpus_fname, "r") as f:
        for line in f:
            tokens = line.strip().split()
            for token in tokens:   # 빈도 수 세기 
                words_count[token] += 1
                total_count += 1
    return words_count, total_count