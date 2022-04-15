''' while 문을 활용하여 해당하는 값 모두 제거 '''
list_test = [1, 2, 1, 2, 3, 2, 4]
value = 2 

while value in list_test:
    list_test.remove(value)

print(list_test)
