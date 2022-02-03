''' 표준 입력으로 두 개의 정수 n과 m이 주어질 때, 별(*) 문자를 이용해 
    가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력 
    
    * n과 m은 각각 1000 이하인 자연수 '''

''' 나의 풀이 '''
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*' * a)

''' 모범 답안 -> for문 사용 x '''
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)