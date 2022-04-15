''' String형 배열 seoul의 element 중 'Kim'의 위치 x를 찾아, 
    "김서방은 x에 있다"는 String을 반환하는 함수 solution을 완성 
    (Seoul에 'Kim'은 오직 한 번만 나타나며 잘못된 값이 입력되지 x)

    seoul:['Jane','Kim'] -> '김서방은 1에 있다'

    * seoul은 길이 1 이상, 1000 이하인 배열 
      seoul의 원소 = 길이 1이상, 20 이하인 문자열 '''

''' 나의 풀이 '''
def solution(seoul):
    answer = ''
    for i, data in enumerate(seoul):
        if data == 'Kim':
            answer ='김서방은 {}에 있다'.format(i)
    return answer

''' 모범 답안 -> '''
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(findKim(['Queen', 'Tod', 'Kim']))