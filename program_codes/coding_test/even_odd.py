''' 정수 num이 짝수일 경우 'Even'을 반환하고 홀수인 경우 'Odd'를 
    반환하는 함수, solution 완성 
    
    * num은 int 범위의 정수, 0 = 짝수 '''

''' 나의 풀이 '''
def solution(num):
    answer = ''
    if num %2 == 0:
        return 'Even'
    else:
        return 'Odd'

''' 모범 답안 '''
def solution(num):
    return 'Odd' if num%2 else 'Even'

print(solution(3))