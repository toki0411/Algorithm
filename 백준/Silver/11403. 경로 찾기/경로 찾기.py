from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            graph[i].append(j)
def dfs(v, x):
    for i in graph[x]:
        if ans[v][i] == 0:
            ans[v][i] = 1
            dfs(v, i)

for i in range(n):
    dfs(i,i)
    print(*ans[i])

