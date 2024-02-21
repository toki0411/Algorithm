from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
ans = 0
q = deque()
q.append((x-1, 0))
visited[x-1] = -1
while q:
    nx, cnt= q.popleft()
    for i in graph[nx]:
        if visited[i]==0:
            q.append((i, cnt+1))
            visited[i] = cnt+1
key = False
for i in range(n):
    if visited[i] == k:
        print(i+1)
        key = True
if not key:print(-1)