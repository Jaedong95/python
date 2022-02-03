n = int(input())
s = input() 
MOD = 1234567891

def solution(s: str) -> int:
    sum = 0 
    for i,d in enumerate(s): 
        if 'a' <= d and d <= 'z':
            sum += ((ord(d)-96) * (31 ** i) % MOD)
        else:
            continue
    print(sum)

solution(s)