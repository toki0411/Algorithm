from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[1000000000] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if graph[nx][ny] and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            elif graph[nx][ny] == 0 and visited[nx][ny] > visited[x][y] :
                visited[nx][ny] = visited[x][y]
                q.append((nx, ny))

bfs()
print(visited[n-1][m-1])