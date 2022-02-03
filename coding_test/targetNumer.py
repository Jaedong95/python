from itertools import permutations

def solution(numbers, target):
    number_list = numbers.copy()
    for i in numbers:
        minus_val = (0 - i)
        number_list.append(minus_val)
    
    print(number_list, numbers)
    val = set(tuple(permutations(number_list, len(numbers))))
    count = 0
    for i in val:
        if sum(i) == target:
            count += 1 
    print(len(val))

solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3)