from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
            elif graph[nx][ny]:
                find[nx][ny] += 1
def bfs_check(x, y, tmp):
    q = deque()
    q.append((x, y))
    visited[x][y] = tmp
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if visited[nx][ny] == 0 and graph[nx][ny]:
                visited[nx][ny] = tmp
                q.append((nx, ny))

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

while True:
    visited = [[0] * m for _ in range(n)]
    # 얼음이 두 덩이가 되었는지 체크
    # 얼음이 다 녹았는지 체크
    key = False
    chunk = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                key = True
                if not visited[i][j]:
                    bfs_check(i, j, chunk)
                    chunk += 1

    if chunk > 2:
        break
    if not key:
        year = 0
        break

    visited = [[0] * m for _ in range(n)]
    # 0이면서 아직 방문하지 않은 바다(0)를 찾아 bfs
    find = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and not visited[i][j]:
                bfs(i, j)
    for i in range(n):
        for j in range(m):
            graph[i][j] -= find[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    year += 1
print(year)