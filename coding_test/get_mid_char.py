''' 단어 s의 가운데 글자를 반환하는 함수, solution 완성 
    단어의 길이가 짝수라면 가운데 두 글자를 반환 
    
    * s는 길이가 1 이상, 100 이하인 스트링 '''

''' 나의 풀이 '''
def solution(s):
    answer = ''
    answer = s[len(s) // 2] if len(s) %2 != 0 else s[(len(s) // 2) - 1] + s[len(s) // 2]
    return answer

''' 모범 답안 -> list slicing '''
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]

print(string_middle("power"))