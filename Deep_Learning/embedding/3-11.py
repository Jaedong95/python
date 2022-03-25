''' 
네이버 영화 리뷰 데이터셋을 전처리하는 코드 
'''

corpus_path = '/notebooks/embedding/data/raw/ratings.txt'
output_fname = '/notebooks/embedding/data/processed/processed_ratings.txt'
with_label = False    # label 값을 함께 저장하고 싶다면 True로 지정 

with open(corpus_path, 'r', encoding='utf-8') as f1, \
                open(output_fname, 'w', encoding='utf-8') as f2:
    next(f1)  # skip head line
    for line in f1:
        _, sentence, label = line.strip().split('\t')   # tab 단위로 line 분리 
        if not sentence: continue   # 문장이 아닐 경우 다음 줄로 넘어감 
        if with_label:   # label이 있다면 label도 같이 출력 
            f2.writelines(sentence + "\u241E" + label + "\n")
        else:    # label이 없다면 문장만 출력 
            f2.writelines(sentence + "\n")