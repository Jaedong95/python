'''
가장 관련성이 높은 영화 추출 
'''
# 36843: 러브 액츄얼리 
# 실행결과 우리, 사랑일까요 ? 노팅 힐, 내 남자의 로맨스 추출 
model.most_similar(36843, topn=3)