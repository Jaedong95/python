from datetime import date 

a_year = int(input('년도를 입력하시오: '))
a_month = int(input('월을 입력하시오: '))
a_day = int(input('일을 입력하시오: '))

day_of_week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
print(day_of_week[date(a_year, a_month, a_day).weekday()])
# print(f'{a_year}년 {a_month}월 {a_day}일은 {day_of_week[date(a_year, a_month, a_day).weekday]}')