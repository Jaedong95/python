import collections 

def solution(dict_graph: dict, v: int):
    graph = dict_graph
    def dfs(v: int, discovered = []) -> list:
        discovered.append(v)
        for w in graph[v]:
            if w not in discovered:
                discoverd = dfs(w, discovered)
        return ' '.join(map(str, discovered))

    def bfs(v: int) -> str:
        discovered = [v]
        queue = [v] 
        while queue:
            v = queue.pop(0)
            for w in graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return ' '.join(map(str, discovered))

    dfs_list = dfs(v, [])
    print(dfs_list)
    bfs_list = bfs(v)
    print(bfs_list)

# 입력 값을 입력받고, 그래프 생성 
n, m, v = map(int, input().split())
graph = collections.defaultdict(list)

count = 0
while True:
    if count == m:
        break
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    count += 1 

# 정점 번호가 낮은 순으로 출력해야 하기 때문에, 정렬한다.
for i in graph:
    graph[i].sort()

solution(graph, v)