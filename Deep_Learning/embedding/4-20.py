'''
PPMI 행렬에 LSA 적용 
'''
from sklearn.decomposition import TruncatedSVD
from soynlp.word import pmi 

# min_mpi보다 낮은 PMI 값은 0으로 치환 
ppmi_matrix, _, _ = pmi(input_matrix, min_pmi=0)   
ppmi_svd = TruncatedSVD(n_componetns=100)   # 차원수 = 100으로 축소 
ppmi_vecs = ppmi_svd.fit_transform(input_matrix)  

# 최종적으로 단어수 x 100 크기의 단어 임베딩 행렬이 만들어짐 