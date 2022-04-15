''' n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운 정수를 리턴하는 
    함수 solution 완성. 
    
    n = 118372 -> 873211 return 
    
    * n은 1이상 8000000000이하인 자연수'''

''' 나의 풀이 '''
def solution(n):
    list = [str(n)[i] for i in range(len(str(n)))]
    list.sort(reverse=True)
    answer = ''
    for x in list:
        answer += x 
    return int(answer)

''' 모범 답안 -> join 연산자 이용 (리스트 이어붙이기) '''
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

print(solution(133456))