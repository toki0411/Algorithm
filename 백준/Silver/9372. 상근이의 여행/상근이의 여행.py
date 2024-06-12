import sys
input = sys.stdin.readline
T = int(input())
def dfs(now, cnt):
    visited[now] = 1
    for node in graph[now]:
        if visited[node] == 0:
            cnt = dfs(node, cnt + 1)
    return cnt

for t in range(T):
    N, M = map(int, input().split()) #국가의 수, 비행기의 종류
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (N+1)
    print(dfs(1, 0))