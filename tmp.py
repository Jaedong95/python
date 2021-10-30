score = int(input('점수를 입력하세요: '))
if score >= 81 and score <= 100:
    print('A')
elif score >= 61 and score <= 80:
    print('B')
elif score >= 41 and score <= 60: 
    print('C')
elif score >= 21 and score <= 40:
    print('D')
elif score >= 0 and score <= 20:
    print('F')
else:
    print('제대로 된 점수를 입력하세요.')