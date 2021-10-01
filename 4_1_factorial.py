def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num-1)

def solution(n: int) -> int:    
    sum = 0 
    for i, d in enumerate(str(n)): 
        sum += int(d) * factorial(len(str(n)) - i)
    return sum 

while True: 
    num = int(input())
    if num == 0:
        break
    print(solution(num))