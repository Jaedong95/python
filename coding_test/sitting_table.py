''' Q.패밀리 레스토랑에서 여러 개의 테이블에 나누어 앉는데, 한 사람만
      앉는 테이블이 없게 그룹. 누가 어디에 앉는지 등은 고려하지 x 
        
      한 개의 테이블에 앉을 수 있는 최대 사람 수는 10명이라고 할 때, 
      100명의 사람이 하나 이상의 테이블에 앉는 패턴을 구하라 '''

# tip = 재귀함수를 사용해 모든 경우를 구함 
min_people = 2
max_people = 10 
total_people = 100 
memo = {} 

def solution(not_sit, sit):
    key = str([not_sit, sit])
    if key in memo:
        return memo[key]
    if not_sit < 0:
        return 0
    elif not_sit == 0:
        return 1 
    
    count = 0 
    for i in range(sit, max_people + 1):
        count += solution(not_sit - i, i)

    # 메모화 처리 
    memo[key] = count 
    return count 

print(solution(total_people, min_people))