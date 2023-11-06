n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0; dp = [[0] * n for _ in range(n)]
dp[0][0] =1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[n-1][n-1])
            break
        down_x = i + board[i][j]
        right_y = j + board[i][j]
        if 0 <= down_x < n:
            dp[down_x][j] += dp[i][j]
        if 0<= right_y < n:
            dp[i][right_y] += dp[i][j]
