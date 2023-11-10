from collections import deque

m, n, h = map(int, input().split())  # m은 가로, n은 세로, h는 높이
graph = []
for _ in range(h):
    graph.append([list(map(int, input().split())) for _ in range(n)])
visited = [[[0] * m for _ in range(n)] for __ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()
def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append([nx, ny, nz])
# visited에 0이 있으면 -1 출력
key = False
arr = []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                arr.append([i,j,k])
            elif graph[k][i][j] == 0:
                key = True
for i in range(len(arr)):
    q.append([arr[i][0], arr[i][1], arr[i][2]])

if not key :
    print(0)
    exit(0)
bfs()
ans = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)
            ans = max(graph[k][i][j], ans)
print(ans-1)

