''' 정수를 담고 있는 배열 arr의 평균값을 return하는 함수 solution 완성
    
    * arr은 길이 1 이상, 100 이하인 배열 
      arr의 원소 -10,000 이상 10,000이하인 정수 '''

''' 나의 풀이 '''
def solution(arr): 
    answer = 0
    for i in arr:
        answer += i
    return answer/len(arr)

''' 모범 답안 -> sum, len 이용 '''
def average(list):
    return (sum(list) / len(list))

list = [5, 3, 4]
print('평균값: {}'.format(average(list)))
