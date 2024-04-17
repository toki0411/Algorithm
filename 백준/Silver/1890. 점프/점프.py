import sys
sys.stdin.readline
dx = [0,1]
dy = [1,0]
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]

def dfs(x, y):
    if x == N-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 0
        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            if 0 <= nx < N and 0 <= ny <N:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

dfs(0,0)
print(dp[0][0])