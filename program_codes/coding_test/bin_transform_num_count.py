''' 
Q2. 1~100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 
하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드 ''' 

''' Practice 
l1 = list(range(10))
l2 = ['{:b}'.format(v) for v in l1]
l3 = ['{:b}'.format(v).count('0) for v in l1]
l4 = [v for v in l1 if '{:b}'.format(v).count('0') == 1]
l5 = [v for v in range(1, 101) if '{:b};.format(v).count('0') == 1]

print(l1)
print(l2)

'안녕안녕하세요'.count('안') -> count 메소드 사용 시 문자열을 매개변수로 사용 '''

# Solution 
output = [v for v in range(1, 101) if '{:b}'.format(v).count('0') == 1]

for i in output:
    print('{} : {}'.format(i, '{:b}'.format(i)))

print('합계:', sum(output))
