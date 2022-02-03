''' 자연수 N이 주어지면, N의 각 자릿수의 합을 구해 return 하는 solution 함수 
    완성
    
    N = 123 -> return 6
    
    * N의 범위: 100,000,000 이하의 자연수 '''

''' 나의 풀이 '''
def solution(n):
    result = 0
    for i in range(len(str(n))):
        result += int(str(n)[i])
    return result

''' 모범 답안 '''
def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10) 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)))