from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
N, M = map(int, input().split())
hx, hy = map(int, input().split()); hx -=1 ; hy -= 1
ex, ey = map(int, input().split()); ex -=1 ; ey -= 1
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[[1e8] * 2 for _ in range(M) ] for __ in range(N)]
q = deque()
q.append((hx, hy, 0))
visited[hx][hy][0] = 0
while q:
    x,y,k = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        if k < 1 and graph[nx][ny] == 1 and visited[nx][ny][k+1] > visited[x][y][k] + 1:
            visited[nx][ny][k+1] = visited[x][y][k] + 1
            q.append((nx, ny, k+1))

        elif graph[nx][ny] == 0 and visited[nx][ny][k] > visited[x][y][k] + 1:
            visited[nx][ny][k] = visited[x][y][k] + 1
            q.append((nx, ny, k))
            
ans = min(visited[ex][ey])
print(ans if ans != 1e8 else -1)