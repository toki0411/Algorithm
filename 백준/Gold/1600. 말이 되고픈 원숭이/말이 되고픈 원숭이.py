from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
hx = [-2, -1, 2, 2, -2, 1, 1, -1]
hy = [-1, -2, 1, -1, 1, 2, -2, 2]
K = int(input())
M, N = map(int, input().split())  # 가로 세로
graph = [list(map(int, input().split())) for _ in range(N)]

q = deque()
visited = [[[1e8] * (K + 1) for __ in range(M)] for ___ in range(N)]
q.append((0, 0, 0))
visited[0][0][0] = 0
while q:
    x, y, k = q.popleft()
    if k < K:  #말처럼 뛴다.
        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if graph[nx][ny] == 0 and visited[nx][ny][k+1] > visited[x][y][k] + 1:
                visited[nx][ny][k+1] = visited[x][y][k] + 1
                q.append((nx, ny, k+1))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if graph[nx][ny] == 0 and visited[nx][ny][k] > visited[x][y][k] + 1:
            visited[nx][ny][k] = visited[x][y][k] + 1
            q.append((nx, ny, k))
ans = min(visited[N-1][M-1])
print(ans if ans != 1e8 else -1)