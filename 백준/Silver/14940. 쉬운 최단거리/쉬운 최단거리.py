from collections import deque
INF = 1e8
n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
x, y = 0, 0
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        if arr[j] == 2:
            x = i
            y = j
    graph.append(arr)

visited = [[INF] * m for i in range(n)]
q = deque()
q.append([x, y])
visited[x][y] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] > visited[x][y] + 1 :
            q.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end = ' ')
        elif visited[i][j] == INF:
            print(-1, end = ' ')
        else:
            print(visited[i][j], end = ' ')
    print()