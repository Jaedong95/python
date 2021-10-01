def get_num(num: str) -> int:
    if num.isnumeric():
        return int(num)
    elif 'A' <= num and num <= 'Z':
        return (ord(num) - 55) 

def solution(num: str, b: str) -> int:
    sum = 0
    for i, d in enumerate(num): 
        val = get_num(d)
        sum += val * (int(b) ** (len(num) - i - 1))
    print(sum)

num, b = input().split()
solution(num, b)