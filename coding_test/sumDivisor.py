''' 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수 작성 

    * n은 0 이상 3000 이하인 정수 '''

''' 나의 풀이 '''
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer

''' 모범 답안 '''
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

print(sumDivisor(12))