''' 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없음
    -> 최대한 많은 부서의 물품을 구매 해 줄 수 있도록 하며, 물품을 구매해
    줄 때는 각 부서가 신청한 금액만큼 모두 지원해 줘야 함. 부서별로 신청한 
    금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 
    개의 부서에 물품을 지원할 수 있는지 return하는 solution 함수 완성 

    * d: 부서별로 신청한 금액이 들어있는 배열, 길이(전체 부서의 개수) = 1 ~ 100 
      d의 각 원소: 부서별 신청 금액, 1 ~ 100,000이하의 자연수 
      budget: 예산, 1 ~ 10,000,000 이하의 자연수 '''

''' 나의 풀이 -> 배열을 정렬해서 앞에서부터 차례대로 더해가며 예산과 비교 '''
def solution(d, budget):
    sum_calc = 0; i = 0
    # d를 모두 다 더했는데도 예산에 미치지 못하는 경우 
    if sum(d) < budget:
        return len(d)
    else:  # else 제거해도 될 듯 ? 
        while sum_calc < budget:
            sum_calc += sorted(d)[i]
            if sum_calc > budget:
                return i 
            i += 1 
        return i

''' 모범 답안 -> pop 이용 '''
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()   # 맨 큰 애들부터 차례대로 제거 
    return len(d)