import csv, random
from scratch.linear_algebra import Vector, distance
from typing import List

with open('./linear_regression/data2.csv') as f:
    reader = csv.reader(f)
    air_x = []
    air_y = []
    air_yt = []
    air_tmp = []
    air_data = []
    # parse_air(row) # -> ['20180101','101', ... ,'0.003'] normal
    for i, row in enumerate(reader):
        #print(row[5:-3])  # ufdust = row[6]
        if i != 0:
            air_tmp.append(row[5:-3])
            air_yt.append(row[6])
        #print(air_x); print(air_y)

    for i, row in enumerate(air_tmp):
        del row[1]
        row.insert(0,1)
        #print(row)
        row = [float(i) for i in row]
        #print(row)
        air_x.append(row)

    air_y = [float(i) for i in air_yt]

    #print(air_y)


def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def predict(x_i, beta):
    return dot(x_i, beta)


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]


#경사하강법에서 오류를 최소화하기 위함
def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)


def squared_error(x_i, y_i, beta):
    return error(x_i, y_i, beta) ** 2


def squared_error_gradient(x_i, y_i, beta):
    return [-2* x_ij * error(x_i, y_i, beta)
            for x_ij in x_i]


def in_random_order(data):
    # Stochastic Gradient Descent 수행을 위한 함수로,
    # 한번 반복문을 돌 때마다 임의의 순서로 데이터 포인트를 반환
    # 데이터 포인트의 인덱스를 list로 생성
    indexes = [i for i, _ in enumerate(data)]
    # 이 인덱스를 랜덤하게 섞는다
    random.shuffle(indexes)
    # 이 순서대로 데이터를 반환한다
    for i in indexes:
        yield data[i]


def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    # SGD 방식으로 gradient descent
    # minimize_batch보다 훨씬 빠르다

    data = zip(x, y)
    # theta_0를 초기 theta로
    theta = theta_0
    # alpha_0를 초기 이동거리(step_size)로
    alpha = alpha_0
    # 시작할 때의 최소값
    min_theta, min_value = None, float("inf")
    iterations_with_no_improvement = 0

    # 만약 100번 넘게 반복하는 동안 value가 더 작아지지 않으면 멈춤
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

        # 새로운 최솟값을 찾았다면
        if value < min_value:
            # 이 값을 저장
            min_theta, min_value = theta, value
            # 100번 카운트도 초기화
            iterations_with_no_improvement = 0
            # 기본 이동거리로 돌아감
            alpha = alpha_0

        # 만약 최솟값이 줄어들지 않는다면
        else:
            # 이동거리 축소
            alpha *= 0.9
            # 100번 카운트에 1을 더함
            iterations_with_no_improvement += 1

        # 반복문이 돌 때마다 in_random_order를 호출하기 때문에
        # 매 iter마다 그래디언트를 계산하는 순서가 달라짐
        for x_i, y_i in in_random_order(data):
            # 각 데이터 포인트에 대해 그래디언트를 계산
            gradient_i = gradient_fn(x_i, y_i, theta)
            # 기존 theta에서, 학습률(alpha)과 그래디언트를 뺀 것을 업데이트
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def estimate_beta(x, y):
    beta_initial = [random.random() for x_i in x[0]]
    return minimize_stochastic(squared_error, squared_error_gradient, x, y, beta_initial, 0.001)


def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))


def multiple_r_squared(x, y, beta):
    sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2
                                for x_i, y_i in zip(x, y))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)

random.seed(0)
beta = estimate_beta(air_x, air_y)  # 예측에 사용한 컬럼: 상수항, fdust, ozone, nd, cm, sagas
print("beta:", beta)

mrs = multiple_r_squared(air_x, air_y, beta)
print("R 제곱:",mrs )
