''' 5초 동안 반복하기 
    # 시간을 기반으로 조건을 걸 때는 while 반복문 활용 '''

import time 

number = 0 

target_tick = time.time() + 5 
while time.time() < target_tick:
    number += 1 

print('5초 동안 {}번 반복했습니다.'.format(number))

    