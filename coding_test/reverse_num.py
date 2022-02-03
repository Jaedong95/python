''' 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴
    
    n = 12345 -> [5,4,3,2,1] return 
    
    * 제한사항: n은 10,000,000,000이하인 자연수 '''

''' 나의 풀이 '''
def solution(n):
    answer = []
    n_str = list(str(n))
    for x in range(1,len(n_str)+1):
        answer.append(int(n_str[-x]))
    return answer

''' 모범 답안 -> map, reversed 이용 '''
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

print(digit_reverse(1314042))