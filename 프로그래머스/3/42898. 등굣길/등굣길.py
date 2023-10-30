def dfs(x, y, dp):
    if x < 0 or y < 0 or dp[y][x] == -1:
        return 0
    if dp[y][x] == 0:
        dp[y][x] = dfs(x - 1, y, dp) + dfs(x, y - 1, dp)
    return dp[y][x]


def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for p in puddles:
        x, y = p
        dp[y-1][x-1] = -1
    dp[0][0] = 1
    ans = dfs(m - 1, n - 1, dp)
    return ans % 1000000007