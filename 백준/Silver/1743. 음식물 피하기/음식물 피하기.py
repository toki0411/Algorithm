import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[0] * (m) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y] = True
    global cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                q.appendleft((nx, ny))
                visited[nx][ny] = True
                cnt +=1
    return cnt
ans = 0
for i in range(n):
    for k in range(m):
        if graph[i][k] == 1 and not visited[i][k]:
            cnt = 1
            trash = bfs(i,k)
            ans = max(trash, ans)

print(ans)

