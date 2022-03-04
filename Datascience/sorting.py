''' 선택 정렬 (Selection Sort) ''' 
def ssort_1(s):
    if s != []: 
        smallest = min(s)
        s.remove(smallest)   # 숫자 제거 
        return [smallest] + ssort_1(s)
    else:
        return [] 

# 꼬리 재귀
def ssort_2(s):
    def loop(s, ss):   # 추가해 줄 애들 
        if s != []:
            smallest = min(s) 
            s.remove(smallest)
            return loop(s, ss + [smallest])   # 원래 있던 애보다 작음 (누적)
        else:
            return ss 
    return loop(s, [])


# while 문 이용 
def ssort_3(s):
    ss = []
    while s != []:
        smallest = min(s)
        s.remove(smallest)
        ss.append(smallest)
    return ss 

s = [10, 2, 3, 65, 4]
print(ssort_2(s))


''' 삽입 정렬 (Insertion Sort) '''
# insert(): 정렬된 리스트 ss의 적절한 위치에 x를 삽입하여 리스트 반환 
# 1. ss를 선두원소 ss[0], 후미리스트 ss[1:]로 나눔 
# 2. x가 선두원소 ss[0]보다 작거나 같으면 ss의 앞에 붙임 
# 3. x가 선두원소 ss[0]보다 크면 를 후미리스트 ss[1:]의 제 위치에 삽입하고, 맨 앞에 선두원소 ss[0]을 붙임 
# * ss가 빈 리스트인 경우, x만 이용하여 리스트를 만듦
def insert(x, ss):
    pass 

def isort_1(s):
    if s != []:
        return insert(s[0], isort_1(s[1:]))
    else: 
        return []

''' 합병 정렬 (Merge Sort) '''
def msort(s):
    if len(s) > 1:
        mid = len(s) // 2
        return merge(msort(s[:mid], s[mid:]))
    else:
        return s 

# merge(): 정렬되어 있는 두 리스트를 비교하며 하나의 정렬된 리스트로 합치고, return 
# 1. 각 리스트의 맨 앞에 있는 두 수 중에서 작은 수를 하나 빼내어 정렬된 리스트를 생성
# 2. 해당 과정을 두 리스트 중에서 하나가 소진될 때 까지 계속 반복 
# 3. 둘 중 하나가 소진되면 나머지를 정렬된 리스트 뒤에 붙임 

def merge(left, right):
    if not ((left == []) or (right == [])):   # left, right 양쪽에 최소한 하나의 원소가 있을 경운
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:], right)
        else:
            return [right[0]] + merge(left, right[1:])
    else:
        return left + right 


''' 퀵 정렬 (Quick Sort) '''
def qsort(s):
    if len(s) > 1:
        pivot = s[0] 
        (left, right) = partition(pivot, s[1:])
        return qsort(left) + [pivot] + qsort(right)
    else:
        return s 

# partition(): pivot 값 기준으로 작은 애들은 왼쪽, 큰 애들은 오른쪽에 배치하여 left, right 리스트 반환 
def partition(pivot, s):
    left, right = [], []
    for x in s:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, right 

''' 버블 정렬 (Bubble Sort) '''
