def dfs(v, n, graph):
    visited[v] = True 
    for i in graph[v]:
        if not visited[i]:
            dfs(i, n, graph)
    
def solution(n, computers):
    global cnt
    cnt = 0
    global visited
    visited = [0] * n
    graph = [[] for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i==j:
                continue
            elif computers[i][j]==1:
                graph[i].append(j)
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i, n, graph)
    return cnt