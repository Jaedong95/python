''' 대문자와 소문자가 섞여있는 문자열 s가 주어질 때, s에 'p'의
    개수와 'y'의 개수를 비교해 True 다르면 False를 return 하는
    solution 함수 완성 'p', 'y' 모두 하나도 없는 경우는 True를 return 
    (개수를 비교할 때 대문자와 소문자는 구별하지 x)
    
    * 문자열 s의 길이: 50 이하의 자연수, 문자열 s는 알파벳으로만 이루어져 있음 '''

''' 나의 풀이 '''
def solution(s):
    answer = True
    s_cnt=0; y_cnt=0
    for i in range(len(s)):
        if s[i] in ['p','P']:
            s_cnt += 1
        elif s[i] in ['y','Y']:
            y_cnt += 1
    return False if s_cnt != y_cnt else True

''' 모범 답안 -> lower, count 적용 '''
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )