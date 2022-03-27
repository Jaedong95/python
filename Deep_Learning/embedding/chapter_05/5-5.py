'''
SVD
204 x 37143의 희소 행렬 -> 204 x 100 크기의 밀집행렬로 선형변환 
'''
from sklearn.decomposition import TruncatedSVD

svd = TruncatedSVD(n_components=100)   # 100차원 
vecs = svd.fit_transform(input_matrix)  # 선형변환 