''' 피보나치 수열 '''
dictionary =  {
    1: 1,
    2: 1
}

def fibonacci(n):
    global counter
    counter += 1 

    if n in dictionary:
        return dictionary[n]
    else: 
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output 
        return output 

counter = 0 
print('fibonacci({})는 {} 입니다.'.format(50, fibonacci(50)))
print('fibonacci({})을 구하는 데 사용된 연산 횟수는 {}번 입니다.'.format(50,counter))

# * 같은 값을 한 번만 수행하도록 코드 작성 (메모화) 

''' factorial '''
dictionary = {
    1:1 
}

def factorial(n):
    global counter
    counter += 1 

    if n in dictionary:
        return dictionary[n]
    else:
        output = n * factorial(n-1)
        dictionary[n] = output 
        return output 

counter = 0
print('factorial({}):{}, 수행횟수:{}'.format(5, factorial(5), counter))