'''
def solution(numbers, target):
sasd    result = []
    def dfs(c_calc, numbers, index, path):
        if len(path) == len(numbers):
            if c_calc == target:
                result.append(path)
                return 
            else:
                return asd
 
        dfs(c_calc+numbers[index], numbers, index+1, path + [numbers[index]])
        dfs(c_calc-numbers[index], numbers, index+1, path + [-numbers[index]])
        
    dfs(0,numbers, 0, [])sas
    return len(result)'''

''' stack '''
def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + (-1) * n)
        q = s.copy()
        print(q)
    return q

solution([1, 1, 1, 1, 1], 3)