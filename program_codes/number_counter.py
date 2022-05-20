# numbers 내부에 들어있는 숫자가 몇 번 등장하는지 출력
numbers = [
    1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 
    4, 9, 7, 2, 1, 3, 5, 4, 8, 9,
    7, 2, 3
]
counter = {}
asd
# A1. if문 사용 
''' 의사코드
for number in numbers:sadsad
    만약 number가 counter 사전의 키라면:
        해당 키의 값을 1 증가
    아니라면:
        counter 사전에 number를 키, 값을 1로 하는 요소 추가 
'''saasdasd
asdasd
for number in numbers:
    if number in counter:
        counter[number] += 1 
    else:
        counter[number] = 1
        
# A2. dict.get() 메서드 사용 
for number in numbers:
    counter[number] = counter.get(number,0) + 1 

print(counter)
