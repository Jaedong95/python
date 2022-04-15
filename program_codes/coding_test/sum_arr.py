''' 2개의 행렬 arr1과 arr2를 입력받아 행렬 덧셈의 결과를 반환하는 함수 solution 완성 
    (행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과)

    * 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 x ''' 

''' 나의 풀이 -> 실패 '''
def solution(arr1, arr2):
    answer = [[]]
    arr1 + arr2 
    return

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

# print(type(arr1),type(arr2))
# print(arr1 + arr2)
print(sum(arr1,arr2))

''' 모범 답안 1 -> zip 함수 사용 '''
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))

''' 모범 답안 2 -> numpy 사용 '''
import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))