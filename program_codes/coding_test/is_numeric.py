''' 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수 
    solution 완성 
    
    s = 'a234' -> False return, s = '1234' -> True return 
    
    * s는 길이 1 이상, 길이 8이하인 문자열 '''

''' 나의 풀이 '''
def is_numeric(s):
    num = ['0','1','2','3','4','5','6','7','8','9']
    
    for i in range(len(s)):
        if s[i] not in num:
            return False   
    return True 

def solution(s):
    if (len(s) == 4 or len(s) == 6) and is_numeric(s):
        return True 
    return False 

print(is_numeric('12345'))

''' 모범 답안 -> s.isdigit(), or -> in '''
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

print( alpha_string46("a234") )
print( alpha_string46("1234") )