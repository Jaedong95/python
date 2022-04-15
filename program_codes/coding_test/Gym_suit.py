''' 일부 학생이 체육복으 도난당했고, 여벌 체육복이 있는 학생이 이들에게 체육복을 
    빌려주려 한다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞 번호의 학생이나
    바로 뒷 번호의 학생에게만 체육복을 빌려줄 수 있음. 체육복이 없으면 수업을 들을 
    수 없기 때문에, 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 함
    
    전체 학생 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을
    가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 
    수 있는 학생의 최댓값을 return 하도록 solution 함수 완성 

    4번 학생 -> 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있음 

    * 전체 학생의 수: 2명 이상 30명 이하
      체육복을 도난당한 학생의 수: 1명 이상 n명 이하 (중복 x)
      여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있으며, 하나만 도난당했다고 가정 
'''

''' 나의 풀이 -> 실패'''
def solution(n, lost, reserve):
    tmp = [i for i in reserve] 
    for i in tmp:
        if (i+1) in lost:
            lost.remove(i+1)
            reserve.remove(i)
        elif i in lost:
            lost.remove(i)
            reserve.remove(i)
    # print(tmp)
    print(lost, reserve)
    if len(reserve) == 0:
        # print('finished')
        return (n-len(lost))
    for i in reserve:
        # print(i)
        if (i-1) in lost:
            lost.remove(i-1)
            
    return (n-len(lost))

''' 강사님 코드 -> set 이용 '''
def solution(n, lost, reserve):
    # 빌릴 필요 x 
    s = set(lost) & set(reserve)
    # 빌려야 함 
    l = set(lost) - s 
    # 빌려줄 수 o
    r = set(reserve) - s 
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    
    return n - len(l)

''' 모범 답안 -> 2번의 for 문 '''
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer