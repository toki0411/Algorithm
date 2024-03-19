import sys
input = sys.stdin.readline
from collections import deque
INF = 10000000
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dirx = [[-1, 0, 0], [1, 0, 0], [-1, 1, 0], [-1, 1, 0]]
diry = [[0, -1, 1], [0, -1, 1], [0, 0, -1], [0, 0, 1]]

n = int(input())
cnt = 2
graph = [list(map(int, input().split())) for _ in range(n)]


def graphColoring(x, y):
    q = deque()
    q.append([x, y])
    graph[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = cnt


def bfs(xx, yy, k):
    q = deque()
    q.append((xx, yy))
    visited = [[INF] * n for _ in range(n)]
    visited[xx][yy] = 0
    while q:
        x, y = q.popleft()
        if graph[xx][yy] != graph[x][y] and graph[x][y] != 0:
            return visited[x][y]
        for i in range(3):
            nx = x + dirx[k][i]
            ny = y + diry[k][i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if visited[nx][ny] > visited[x][y] + 1 and graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            elif visited[nx][ny] > visited[x][y] + 1 and graph[nx][ny] != graph[xx][yy]:
                visited[nx][ny] = visited[x][y]
                q.append((nx, ny))
    return INF

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graphColoring(i, j)
            cnt += 1
ans = INF
for k in range(4):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                nx = i + dx[k]
                ny = i + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
                if graph[nx][ny] == 0:
                    tmp = bfs(i, j, k)
                    ans = min(tmp, ans)
print(ans)