''' 수포자 3인방은 모의고사에 수학 문제를 전부 찍으려 하며, 1번 문제부터
    다음 문제까지 다음과 같이 찍음. 1번 문제부터 마지막 문제까지의 정답이
    순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 
    누구인지 배열에 담아 return 하도록 solution 함수 완성 
    
    1번 수포자 -> 1,2,3,4,5,1,2,3,4,5,...
    2번 수포자 -> 2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5,... 
    3번 수포자 -> 3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5, ... 
    
    * 시험은 최대 10,000 문제로 구성되어 있으며, 문제의 정답은 1,2,3,4,5 중 하나  
      가장 높은 점수를 받는 사람이 여럿일 경우, return하는 값을 오름차순 정렬 '''

''' 나의 풀이 '''
def solution(answers):
    answer = []
    score_p1 = 0; score_p2 = 0; score_p3 = 0
    math_p1 = [1,2,3,4,5] # * 200 
    math_p2 = [2,1,2,3,2,4,2,5] # * 125 
    math_p3 = [3,3,1,1,2,2,4,4,5,5] # * 100 
    # answers *= 200 
    
    for i in range(len(answers)):
        if answers[i] == math_p1[i]:
            score_p1 += 1 
        if answers[i] == math_p2[i]:
            score_p2 += 1
        if answers[i] == math_p3[i]:
            score_p3 += 1 
            
    scores = [score_p1, score_p2, score_p3]
    max_score = max(scores)
    best_p = [x for x in scores if max_score == x] 
    
    if len(best_p) == 1:
        for i, d in enumerate(best_p):
            if d == max_score:
                return [i+1]
    else:
        for i, d in enumerate(best_p):
            if d == max_score:
                answer.append(i+1)
        return answer

''' 모범 답안 -> % 연산 이용 '''
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    print(result)
    return result

solution([1,2,3,4,5])