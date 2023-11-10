from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x, y, h):
    q = deque([(x,y,h)])
    while q:
        x,y,h= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] > h:
                visited[nx][ny]=1
                q.append([nx,ny,h])
max_cnt = 0
for height in range(0, 101):
    visited = [[0] * n for _ in range(n)]
    safe_cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > height:
                safe_cnt += 1
                bfs(i, j, height)
    max_cnt = max(safe_cnt, max_cnt)

print(max_cnt)
