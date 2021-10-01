n = int(input())

def factorial(n: int) -> int:
    if n == 1:
        return 1 
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))