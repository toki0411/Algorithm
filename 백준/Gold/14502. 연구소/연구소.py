from collections import deque
import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0


def bfs():
    global ans
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append([i, j])
    graph2 = copy.deepcopy(graph)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph2[nx][ny] == 0:
                graph2[nx][ny] = 2
                q.append([nx, ny])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph2[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)


def makeWall(cnt, x, y):
    if cnt == 3:
        bfs()
        return
    for i in range(x, n):
        if x != i:
            y = 0
        for j in range(y, m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt + 1, i, j)
                graph[i][j] = 0


makeWall(0, 0, 0)
print(ans)