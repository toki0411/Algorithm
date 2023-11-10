from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
ans = [[0] * n for _ in range(n)]
# visited = []* n
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            graph[i].append(j)

for i in range(n):
    q = deque([i])
    while q:
        v = q.popleft()
        for j in graph[v]:
            if ans[i][j] == 0:
                ans[i][j] = 1
                q.append(j)
for i in range(n):
    print(*ans[i])
