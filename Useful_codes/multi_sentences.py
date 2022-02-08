''' 여러 줄 문자열과 구문을 함께 사용할 때 발생하는 문제 (들여쓰기) 해결 
    1. 괄호로 문자열 연결 '''
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다."
)

print('test:',test)
print('type(test):', type(test))

# * 괄호 안 문자열이 쉼표로 연결되어 있을 경우에는 튜플로 취급되기 때문에 주의 ! 

''' 2. 마지막을 제외한 문자열 뒤에 \n 입력 '''
number = int(input("정수 입력> "))

if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))

''' 3. join 함수 사용 - join 함수: 리스트의 요소를 문자열로 연결 '''
number = int(input("정수 입력> "))

if number % 2 == 0:
    print('\n'.join([
        '입력한 문자열은 {}입니다.',
        '{}는(은) 짝수입니다.'
    ]).format(number, number))
else:
    print('\n'.join([
        '입력한 문자열은 {}입니다.',
        '{}는(은) 홀수입니다.'
    ]).format(number, number))