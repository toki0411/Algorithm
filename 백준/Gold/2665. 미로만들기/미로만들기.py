from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    x = 0
    y = 0
    # limit = zeroCnt + 1
    visited = [[1000000] * n for _ in range(n)]
    # visited = [[[1000000 for l in range(limit)] for _ in range(n)] for __ in range(n)] #레벨 m n
    visited[0][0] = 0
    q.append((x, y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] and visited[nx][ny] > visited[x][y]:  #1이면 (흰방)
                visited[nx][ny] = visited[x][y]
                q.append((nx, ny))
            elif graph[nx][ny] == 0 and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return visited[n-1][n-1]

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
zeroCnt = 0
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 0:
#             zeroCnt += 1
print(bfs())