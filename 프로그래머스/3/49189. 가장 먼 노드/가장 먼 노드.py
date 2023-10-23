from collections import deque
def bfs(V,visited,graph):
    q = deque([V]);
    visited[V] = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[v]+1 < visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1
    return
def solution(n, edge):
    ans = 0
    INF = int(1e8)
    visited = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in edge:
        a, b = i[0], i[1]
        graph[a].append(b)
        graph[b].append(a)
    bfs(1,visited,graph)

    visited = visited[1:]
    max_val = max(visited)
    return visited.count(max_val)