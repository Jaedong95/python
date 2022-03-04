''' 리스트 검색, 문자열 검색, 파일 입출력 등에 대한 포스팅 '''
# random.randrange(n): n까지의 수들 중 한 개 정수 임의로 반환 
# random.sample(sequence, k): 시퀀스에서 '중복없이' k개를 무작위로 골라 리스트로 반환

import random

db = random.sample('polulation', 4)
print(db)


''' 순차 검색 '''
# 재귀 
def seq_search_ox(s, key):
    if s != []:
        if s[0] == key:
            return True
        else:
            return seq_search_ox(s[1:], key)
    else: 
        return False 


# 반복문, while 
def seq_search_ox(s, key):
    while s != []:
        if s[0] == key:
            return True
        else:
            s = s[1:]
    return False 

# 반복문, for 
def seq_search_ox(s, key):
    for x in s:
        if x == key:
            return True 
    return False 


# 찾은 위치 반환 
def seq_search(s, key):
    i = 0 
    for x in s:
        if x == key:
            return i 
        i += 1 
    return None 

''' 이분 검색 '''
# 정렬된 리스트를 반으로 나누어 검색하는 방법 
# 1. ss의 정가운데 원소의 위치 번호: mid
# 2. key가 ss[mid]와 같으면 True return
# 3. key가 ss[mid]보다 작으면 ss[:mid]에서 key를 재귀로 찾음
# 4. key가 ss[mid]보다 크면 ss[mid:]에서 key를 재귀로 찾음 

# 재귀 
def bin_search_ox(ss, key):
    if ss != []:
        mid = len(ss) // 2 
        if key == ss[mid]:
            return True 
        elif key < ss[mid]:
            return bin_search_ox(ss[:mid], key)
        else:
            return bin_search_ox(ss[mid+1:], key)
    else:
        return False 

# 반복, while 
def bin_search_ox(ss, key):
    while ss != []:
        mid = len(ss) // 2
        if key == ss[mid]:
            return True
        elif key < ss[mid]:
            ss = ss[:mid]
        else:
            ss = ss[mid+1:]
    return False 


# 찾은 위치 반환
# 검색 범위의 시작과 끝을 알려주는 위치번호(low, high)를 지정하고, 검색 범위를 좁혀가며 탐색 
def bin_search(ss, key):
    low = 0 
    high = len(ss) - 1
    while low <= high:
        mid = (low + high) // 2 
        if key == ss[mid]:
            return mid 
        elif key < ss[mid]:
            high = mid - 1 
        else:
            low = mid + 1 
    return None 

# 찾은 위치 반환 코드 테스트 
def test_bin_search():
    print('Binary search test!') 
    db = random.sample(range(10000), 1000)
    db.sort()
    for i in range(10):
        key = random.randrange(10000)   # 임의의 정수 한 개 반환 
        index = bin_search(db, key)
        print(key, 'found at', index)


''' 파일 입출력 '''
# read(n): 파일에서 문자 n개를 읽어 문자열로 반환
# read(): 파일의 현재 위치에서 그 파일의 맨 끝까지 문자를 모두 반환
# readline(n): 현재 줄에서 n개 문자 읽음 
# readline(): 한 줄을 다 읽음 
# readlines(): 파일을 줄 별로 모두 읽어서 줄의 리스트 반환 
# write(s): 문자열 s를 파일에 기록 
# writelines(ss): 문자열 리스트 ss에 있는 모든 문자열을 모두 파일에 기록 

f = open('output.txt', 'w')
f.write('David Beckham is an English former professional footballplayer.\n')
f.close()

''' 문자열 검색 '''
# str.find(sub): str에서 맨 앞에 나오는 sub의 위치 번호 반환 (없을 경우 return -1)
# str.index(sub): str에서 맨 앞에 나오는 sub의 위치 번호 반환 (없을 경우 ValueError)
# str.rfind(sub): str에서 맨 뒤에 나오는 sub의 위치 번호 반환
# str.startwith(prefix): str이 prefix로 시작하면 True, 그렇지 않을 경우 False 반환
# str.endswith(suffix): str이 suffix로 끝나면 True, 그렇지 않을 경우 False 반환 

sentence = 'David Beckham is an English former professional footballplayer.'
sentence.find('a', 6)   # sentence[6:]에서 'a'가 처음으로 나오는 위치 번호 

# 파일 이름 filename과 찾을 문자열을 받아서 두 번째로 나타나는 위치 번호를 'result.txt' 파일에 작성
def find_second(filename, key):
    infile = open(filename, 'r')
    outfile = open('result.txt', 'w')

    text = infile.read()
    pos = text.find(key)
    pos = text.find(key, pos + 1)   # 두 번째 값 검색

    if pos == -1:
        outfile.write(key + 'is not found.\n')
    else:
        outfile.write(key + 'is at' + str(pos) + 'the 2nd time.\n')
    outfile.close()
    infile.close()
    print('done !') 