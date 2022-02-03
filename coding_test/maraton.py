''' 수 많은 마라톤 선수들이 마라톤에 참여하였으며, 단 한 명의 선수를 제외하고는 
    모든 선수가 마라톤을 완주하였다. 마라톤에 참여한 선수들의 이름이 담긴 배열 
    participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
    완주하지 못한 선수의 이름을 return 하도록 solution 함수 완성 
    
    * 마라톤 경기에 참여한 선수의 수 = 1명 이상 100,000명 이하 
      completion의 길이 = participant의 길이 - 1 
      참가자의 이름: 1개 이상 20개 이하의 알파벳 소문자 
      참가자 중에는 동명이인이 있을 수 있음 '''

''' 나의 풀이 -> 탐색, 효율성 테스트 통과 x '''
def solution(participant, completion):
    # for i in completion:
    for i in range(len(completion)):
        participant.remove(completion[i])
        
    return participant[0]

''' 나의 풀이 -> dict 자료구조 이용한 시도.. 실패 ㅜ '''
def solution(participant, completion):
    participants = {} 
    for i in participant:
        participants[i] = participants.get(i, 0) + 1 
    
    for i, d in participants.items():
        if i in completion:
            participants[i] -= 1 
    
    for i, d in participants.items():
        if d == 1:
            return i 
#     if participants.values() == 1:
#         print(participants.keys())

''' 강사님 풀이 -> dict 자료구조 이용 '''
def solution(participant, completion):
    d = {}
    for x in participant:
       d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1 

    dnf = [k for k, v in d.items() if v > 0]
    answer = dnf[0]
    return answer 

''' 모범 답안 -> collections 모듈의 Counter 이용 '''
import collections 

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

''' 모범 답안2 -> Hash 함수 이용 '''
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

''' 모범 답안3 -> sort 이용 '''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]