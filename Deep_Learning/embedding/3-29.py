'''
코드 3-28 학습 결과를 바탕으로 띄어쓰기 교정을 수행 
'''
from soyspacing.countbase import CountSpace 

model_fname = '/notebooks/embedding/data/processed/space-correct.model'
model = CountSpace()   # 띄어쓰기 모델 클래스 생성 
model.load_model(model_fname, json_format=False)   # 앞서 생성한 모델 로드 
model.correct('어릴때보고 지금다시봐도 재밌어요')    # 띄어쓰기 교정 