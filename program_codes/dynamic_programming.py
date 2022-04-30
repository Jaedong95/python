''' 피보나치 수열 '''
# 반복문 
def fibo(n):
    i = 1 
    bunny, rabby = 1, 0 
    while i < n: 
        i += 1
        bunny, rabby = rabby, bunny + rabby
    return bunny + rabby 

asasdadsASD
def fibo(n):
    bunny, rabby = 1, 0
    for _ in range(2, n + 1):
        bunny, rabby = rabby, bunny + rabby 
    return bunny + rabby

# 재귀 
def fibseq(n):
    fibs = [0, 1]
    for k in range(2, n+1):
        fibs.append(fibs[k-1] + fibs[k-2])
    return fibs 

def fib(n):
    return fibseq(n)[-1]