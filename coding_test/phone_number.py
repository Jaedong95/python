''' 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 
    제외한 나머지 숫자를 전부 '*'으로 가린 문자열을 리턴하는 함수 solution 완성 
    
    * s는 길이 4 이상, 20 이하인 문자열 '''

''' 나의 코드 '''
def solution(phone_number):
    tmp = list(phone_number)
    # str(['*' for x in range(len(tmp)) if (x+ 3) < len(tmp) else tmp[x]])
    answer = []
    for x in range(len(tmp)):
        if (x + 4) < len(tmp):
            answer.append('*')
        else:
            answer.append(tmp[x])
    # print(type(str(''.join(answer))))
    return 

solution("01033334444")

''' 모범 답안 -> 문자열 곱셈 '''
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'))
