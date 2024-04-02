from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                return visited[x][y] + 1
            if graph[nx][ny] == '.' and visited[nx][ny] > visited[x][y] + 1:
                if fire[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return False


def fireSpread(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
            if graph[nx][ny] == '.':
                if fire[x][y] + 1 < fire[nx][ny]:
                    fire[nx][ny] = fire[x][y] + 1
                    q.append((nx, ny))

R,C = map(int, input().split())
INF = 1e8
graph = [list(input()) for _ in range(R)]
visited = [[INF] * C for _ in range(R)]
fire = [[INF] * C for _ in range(R)]
jh = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            fire[i][j] = 0
            fireSpread(i, j)
        elif graph[i][j] == 'J':
            jh = [i, j]
            graph[i][j] = '.'
key = bfs(jh[0], jh[1])
if key:
    print(key)
else:
    print("IMPOSSIBLE")