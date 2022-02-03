''' 각 원소는 숮사 0~9 까지로 이루어져 있는 배열 arr. 
    배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
    (제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서 유지)
    arr = [1, 1, 3, 3, 0, 1, 1] -> [1, 3, 0, 1]
    arr = [4, 4, 4, 3, 3] -> [4, 3] 
    배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 

    * 배열 arr: 1,000,000 '''

''' 나의 풀이 '''
def solution(arr):
    answer = [] 
    arr.append('999999999')
    answer = [arr[i] for i in range(len(arr) - 1) if arr[i] != arr[i+1]]
    return answer 

print(solution([1,3,3,3,3,4,5,6,9,9,8]))

''' 모범 답안 -> 리스트 슬라이싱 '''
def no_continuous(s):
    a = [] 
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a 

print(no_continuous('1330303'))