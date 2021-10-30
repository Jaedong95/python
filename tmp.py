personal_num = input("주민등록번호를 입력하세요: ")
number = personal_num.split('-')
print("남자" if number[1][0] in ['1', '3'] else "여자")