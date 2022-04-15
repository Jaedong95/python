''' 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수 
    solution 완성. 배열의 맨 앞에 최대공약수, 그 다음 최소공배수를 넣어
    반환.
    
    * 두 수는 1이상 1000000이하의 자연수'''

''' 나의 풀이 '''
def solution(n, m):
    if n > m:
        n, m = m, n

    # n의 약수들을 모아둔 리스트 tmp 
    tmp = [i for i in range(1, n + 1) if n % i == 0]

    # m의 약수들 중 tmp에 있으면 리스트에 저장 (최대공약수 계산)
    min = [tmp[i-1] for i in range(1, len(tmp) + 1) if m % tmp[i-1] == 0][-1]

    # n의 배수들이 m의 배수들 중에 있으면 리스트에 저장 (최소공배수 계산)
    max = [i for i in range(n, 10000000, n) if i in range(m, 10000000,m)][0]
    return [min, max]

''' 모범 답안 -> 유클리디안 알고리즘 이용 '''
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

print(gcdlcm(3,12))

''' 모범 답안 2 -> 함수 정의 '''
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))

def gcdlcm(a, b):
    return [gcd(a, b), lcm(a, b)]

print(gcdlcm(3,12))