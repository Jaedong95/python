import numpy as np

''' 기본 배열 '''
np.random.rand(5, 2)   # 5 * 2 랜덤값을 가진 배열, type: numpy.ndarray

np.arange(6)   # array([0, 1, 2, 3, 4, 5])
np.arange(24).reshape(2, 3, 4)

a = np.array([1, 2, 3])   # 1차원 배열 

a = [(1, 2, 3), ('a', 'b', 'c'), ('가', '나', '다')]
b = np.array(a)    # 2차원 배열 

ar = np.array([1, 2, 3, 4], dtype=float)   # 데이터 타입 지정하여 배열 생성 

''' 배열 초기화 '''
# zeros((s), ..): 지정 배열(s) 생성 후 값을 모두 0으로 초기화
# ones((s), ..): 지정 배열(s) 생성 후 값을 모두 1로 초기화
# full((s), n, ..): 지정 배열(s) 생성 후 값을 모두 n으로 초기화 
# empty((s), ..): 지정 배열(s) 생성, 초기값 없음 
# eye(s, ..): 크기가 s인 단위 행렬 생성 
# like(s, ..) 지정 배열(s)와 같은 배열 생성 후 초기화 

a = np.full((2, 3), 10, dtype='int')
print(a) 
# print(np.empty((3, 4)))    # -> 쓰레기 값으로 초기화됨 

s = np.zeros((3, 4))
print(np.ones_like(s))

''' 범위 지정하여 배열 생성 '''
# arange(start, stop, step, ..): 데이터 기준으로 step 간격으로 데이터 생성하고, 배열 지정 
# linspace(start, stop, n, ..): 요소 기준으로 n개만큼 균일하게 배열 생성
# logspace(start, stop, n, ..): 로그 스케일로 n개만큼 균일하게 배열 생성 

a = np.arange(0, 10, 5)   # [0, 5]
b = np.linspace(0, 10, 5)   # [0, 2.5, 5, 7.5, 10]

''' 난수 생성 '''
# random.rand(s): 0~1까지 균등하게 무작위 추출하여 배열(s) 생성 
# random.randint(start, end, (s), ..): 지정된 수 범위에서 정수를 균등하게 추출하여 배열(s) 생성 
# random.randn(s): 정규분포로 수를 추출하여 배열(s) 생성 
# random.noraml(M, SD, (s), ..): 평균(M), 표준편차(SD)를 가지는 정규분포에서 추출하여 배열(s) 생성
# random.shuffle(a): 무작위로 값을 섞음 
# random.choice(range(a), n): 해당 범위에서 무작위로 n개 만큼 추출 

# random.f(분자자유도, 분모자유도, 개수)
# random.chisquare(자유도, 개수): 카이제곱분포에서 값을 추출 
# random.standart_t(자유도, 개수): t분포에서 값을 얻음 

print(f'random.rand(s): \n{np.random.rand(3, 4)}')
print(f'random.randint(start, end, s): \n{np.random.randint(1, 10, (3, 3))}')
print(f'random.randn(s): \n{np.random.randn(5, 5)}')
print(f'random.normal(M, SD, s): \n{np.random.normal(10, 1, (4, 4))}')
print(f'random.choice(range(a), n): {np.random.choice([1, 2, 3, 4, 5], 3)}')
# n * 4 형태의 2차원 매트릭스를 생성하고 해당 매트릭스에 0~100 사이의 값 저장
print(f'random.fill_matrix: {np.random.randint(0, 101, (n, 4))    

a = np.arange(1, 10)
np.random.shuffle(a)
print(f'random.shuffle(a): {a}')

''' 덧셈, 곱셈, 나눗셈, 지수 연산 '''
# a + b, add(a, b)
# a - b, subtract(a, b)
# a / b, divide(a, b)
# a * b, multiply(a, b)
# exp(b): b의 지수를 구함 
# sqrt(a): a의 제곱근을 구함 
# sin(a)
# log(a)
# dot(a, b): 벡터의 내적을 구함 
# a == b 

a = np.linspace(1, 9, 9, dtype=int).reshape(3, 3)
print(a)
b = np.arange(1, 10).reshape(3, 3)
print(np.mean(a, axis=0))