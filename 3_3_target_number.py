def solution(numbers, target):
    result = []
    def dfs(c_calc, numbers, index, path):
        if len(path) == len(numbers):
            if c_calc == target:
                result.append(path)
                return 
            else:
                return 
 
        dfs(c_calc+numbers[index], numbers, index+1, path + [numbers[index]])
        dfs(c_calc-numbers[index], numbers, index+1, path + [-numbers[index]])
        
    dfs(0,numbers, 0, [])
    return len(result)