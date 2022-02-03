''' 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 
    암호화 방식을 시저 암호라고 함. 문자열 s와 거리 n을 입력받아 s를 n만큼 
    민 암호문을 만드는 함수, solution 완성 
    
    'AB'를 거리 1만큼 밀 경우 -> 'BC', 3만큼 밀 경우 -> 'DE' 
    'z'를 거리 1만큼 밀 경우 -. 'a' 
    
    * s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있으며 공백은 아무리 밀어도 공백
      s의 길이는 8000이하이며, n은 1이상, 25이하인 자연수 '''

''' 나의 풀이 '''
def solution(s, n):
    answer = []
    
    # alpha_l을 리스트가 아닌 문자열 자료형으로 했을 경우 좀 더 간단 
    alpha_l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha_u = [x.upper() for x in alpha_l]
    for i in range(len(s)):
        if s[i] == ' ':
            answer.append(s[i])
            continue
        if s[i] in alpha_l:
            # print(type(alpha_l.index(s[i])))
            # print(alpha_l[(alpha_l.index(s[i]) + n) % 26])
            answer.append(alpha_l[(alpha_l.index(s[i]) + n) % 26])
            
        elif s[i] in alpha_u:
            # print(alpha_u[(alpha_u.index(s[i]) + n) % 26])
            answer.append(alpha_u[(alpha_u.index(s[i]) + n) % 26])
    return "".join(answer)

''' 모범 답안 -> ord 사용 '''
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))