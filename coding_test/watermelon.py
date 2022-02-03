''' 길이가 n이고, '수박수박수...'와 같은 패턴을 유지하는 문자열을 리턴하는 함수 
    solution을 완성. 
    
    n = 4 -> '수박수박' return, n = 3 -> '수박수' return 
    
    * n은 길이 10,000 이하인 자연수 '''

''' 나의 코드 '''
def solution(n):
    answer = ''
    for i in range(1,n+1):
        if i % 2 == 0:
            answer += '박'
        elif i % 2 == 1:
            answer += '수'
    return answer

''' 모범 답안 -> 문자열 길이를 2배 늘리고, slicing '''
def water_melon(n):
    s = "수박" * n
    return s[:n]

print("n이 3인 경우: " + water_melon(3))
print("n이 4인 경우: " + water_melon(4))