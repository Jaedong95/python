''' 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 
    지니는 리스트를 리턴하는 함수 solution 완성 
    
    * x는 -10000000 이상, 10000000 이하인 정수 
      n은 1000 이하인 자연수 '''

''' 나의 풀이 '''
def solution(x, n):
    answer = []
    if x > 0:
        answer = list(range(x, x*n + 1,x))
    elif x < 0:
        answer = list(range(x, x*n - 1,x))
    else: 
        for i in range(n):
            answer.append(0)
    return answer

''' 모범 답안 -> range 함수 이용 '''
def number_generator(x, n):
    return [i * x + x for i in range(n)]

print(number_generator(2, 5))
