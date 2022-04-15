''' 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수 solution 완성 
    소수 = 1과 자기 자신으로만 나누어지는 수 
    
    * n = 2이상 1000000이하의 자연수 '''

''' 나의 풀이 -> 시간 초과 '''
def solution(n):
    answer = 0 
    for i in range(2, n + 1): 
        if isprime(i):
            answer += 1 
    return answer 

def isprime(x):
    for i in range(2, x):
        if x % i == 0: 
            return False 
    # print('{} is Prime'.format(x))
    return True 

''' 나의 풀이 -> 재귀로 도전 '''
# ㅜㅡㅜ 

''' 모범 답안 -> 에라토스테네스의 체 사용 '''
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)