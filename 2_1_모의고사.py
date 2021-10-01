def solution(answers):
    answer = []
    score_p1 = 0; score_p2 = 0; score_p3 = 0
    math_p1 = [1,2,3,4,5] # * 200 
    math_p2 = [2,1,2,3,2,4,2,5] # * 125 
    math_p3 = [3,3,1,1,2,2,4,4,5,5] # * 100 
    
    for i in range(len(answers)):
        if answers[i] == math_p1[i % len(math_p1)]:
            score_p1 += 1 
        if answers[i] == math_p2[i % len(math_p2)]:
            score_p2 += 1
        if answers[i] == math_p3[i % len(math_p3)]:
            score_p3 += 1
            
    scores = [score_p1, score_p2, score_p3]
    math_p = [1, 2, 3]
    
    max_s = max(scores)
    for a, b in zip(math_p, scores):
        # print(a, b)
        if b == max_s:
            answer.append(a)
    return sorted(answer)