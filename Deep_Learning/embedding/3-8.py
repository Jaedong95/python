import json 

# corpus file 이름 지정 
corpus_fname = '/notebooks/embedding/data/raw/KorQuAD_v1.0_train.json'
# 출력 파일 이름 지정 
output_fname = '/notebooks/embedding/data/processed/processed_korquad_train.txt'

with open(corpus_fname) as f1, open(output_fname, 'w', encoding='utf-8') as f2:
    dataset_json = json.load(f1)   # corpus file 로드 
    dataset = dataset_json['data']   # data 부분만 추출 
    for article in dataset:   # data에서 기사 부분 추출 
        w_lines = []
        for paragraph in article['paragraphs']:   # 기사의 문맥 단위 추출 
            w_lines.append(paragraph['context'])   # 내용 추가 
            for qa in paragraph['qas']:   # 질문 
                q_text = qa['question']
                for a in qa['answers']:   # 대답 
                    a_text = a['text']
                    w_lines.append(q_text + " " + a_text)
        for line in w_lines:
            f2.writelines(line + "\n")   # 파일 작성 