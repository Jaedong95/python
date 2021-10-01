def solution(participant, completion):
    dict_p = {}
    for i in participant:
        dict_p[i] = dict_p.get(i,0) + 1 
    
    for i in completion:
        dict_p[i] -= 1 
    
    return [i for i, d in dict_p.items() if d > 0][0]