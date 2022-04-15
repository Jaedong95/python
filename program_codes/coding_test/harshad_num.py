''' 양의 정수 x가 하샤드 수이러면 x의 자릿수의 합으로 x가 나누어져야 함.
    자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 solution 함수 완성 
    
    * x는 1 이상, 10000 이하인 자연수 '''

''' 나의 풀이 '''
def solution(x):
    answer = [int(str(x)[i]) for i in range(len(str(x)))]
    return True if x % sum(answer) == 0 else False

''' 모범 답안 '''
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))