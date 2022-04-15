''' 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 return
    하는 함수 solution 완성
    
    * a와 b가 같은 경우 둘 중 아무 수나 return 
      a와 b는 -10,000,000 이상 10,000,000 이하인 정수
      a와 b의 대소관계는 정해져있지 않음 '''
    
''' 나의 풀이 '''
def solution(a, b):
    answer = 0
    if a > b:
        for i in range(b, a + 1):
            answer += i
    else:
        for i in range(a, b + 1):
            answer += i
    return answer

''' 모범 답안 -> swap 이용 '''
def adder(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))

print(adder(3, 5))