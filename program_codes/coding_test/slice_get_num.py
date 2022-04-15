''' 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, 
    k번째에 있는 수를 구하려 함. 배열 array, [i,j,k]를 원소로 가진 
    2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에
    대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return
    하는 solution 함수 완성 
    
    array = [1,5,2,6,3,7,5], i = 2, j = 5, k = 3 
    input: array = [1, 5, 2, 6, 3, 7, 4] commands = [[2,5,3],[4,4,1],[1,7,3]]   
    
    * array의 길이 = 1 이상 100 이하, array의 각 원소 = 1 이상 100 이하 
      commands의 길이 = 1 이상 50 이하, commands의 각 원소 길이 = 3 '''

''' 나의 풀이 '''
def solution(array, commands):
    list_slice = []
    answer = []
    for i in range(len(commands)):
        commands[i][2] -= 1 
        list_slice = array[commands[i][0]-1:commands[i][1]]
        list_slice.sort()
        print(list_slice)
        answer.append(list_slice[commands[i][2]])

    return answer

''' 모범 답안 -> lambda 함수 이용 '''
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))