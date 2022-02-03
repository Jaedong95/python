import collections 

def solution(dict_graph: dict, v: int):
    graph = dict_graph
    def dfs(v: int, discovered) -> list:
        discovered.append(v)
        for w in graph[v]:
            if w not in discovered:
                discovered = dfs(w, discovered)
        return discovered

    dfs_list = dfs(v, [])
    print(len(dfs_list) - 1)

graph = collections.defaultdict(list)
n = int(input())
m = int(input())

count = 0
while True:
    if count == m: 
        break
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    count += 1 

# print(graph)
solution(graph, 1)