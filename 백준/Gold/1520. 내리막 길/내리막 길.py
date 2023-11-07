m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
#m이 세로 n이 가로 arr[m][n], arr[y][x]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
dp = [[-1] * n for _ in range(m)]
# dp[0][0] = 1
def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    else:
        dp[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and not visited[ny][nx] and graph[ny][nx] < graph[y][x]:
                visited[ny][nx] = 1
                dp[y][x] += dfs(nx, ny)
                visited[ny][nx] = 0
    return dp[y][x]
visited = [[0] * n for _ in range(m)]
dfs(0,0)
print(dp[0][0])
