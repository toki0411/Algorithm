N, Ep, Wp, Sp, Np = map(int, input().split())
p = [Ep, Wp, Sp, Np]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[0] * (2*N+1) for _ in range(2*N+1)]
ans = 0
def dfs(x, y, depth, percent):
    global ans
    if depth == N:
        ans += percent
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < 2*N+1 and 0 <= ny < 2*N+1:
            if graph[nx][ny] == 1: continue
            else:
                graph[nx][ny] = 1
                tmp_percent = percent * (p[i]/100)
                dfs(nx, ny, depth + 1, tmp_percent)
                graph[nx][ny] = 0

graph[N][N] = 1
dfs(N, N, 0,1)
print(ans)