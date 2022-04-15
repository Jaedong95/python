''' 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 
    판단하려 함. n이 양의 정수 x의 제곱이라면 x+1의 제곱을 return하고, 
    n이 양의 정수 x의 제곱이 아니라면 -1을 return하는 solution 완성 

    * n은 1이상, n은 1이상, 50000000000000 이하인 양의 정수 ''' 

''' 나의 풀이 -> 틀림 '''
from math import sqrt 

def solution(n):
    if sqrt(n) * sqrt(n) == n:
        return (sqrt(n)+1) ** 2
    else:
        return -1 

''' 모범 답안 -> 제곱근 이용 '''
def nextSqure(n):
    sqrt = n ** (1/2)
    
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2 
    return 'no' 

print (nextSqure(10000))
