def solution(n, lost, reserve):
    # 빌릴 필요 x 
    s = set(lost) & set(reserve)
    # 빌려야 함 
    l = set(lost) - s 
    # 빌려줄 수 o
    r = set(reserve) - s 
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    
    return n - len(l)