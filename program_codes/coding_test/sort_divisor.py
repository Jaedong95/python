''' array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 
    정렬한 배열을 반환하는 함수 solution 완성. divisor로 나누어 떨어지는 
    element가 하나도 없다면 배열에 -1을 담아 반환 
    
    * arr: 자연수를 담은 배열. len(arr) >= 1. divisor = 자연수 
      정수 i, j에 대해 i != j 이면 arr[i] != arr[j] ''' 

''' 나의 풀이 '''
def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer

''' 모범 답안 -> or 활용 '''
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

print(solution([5, 9, 7, 10], 5))