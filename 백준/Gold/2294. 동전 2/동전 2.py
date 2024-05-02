n, k = map(int, input().split())
coin = [0] + [int(input()) for _ in range(n)]
coin.sort()
dp = [[1e9 for _ in range(k + 1)] for __ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j % coin[i] == 0:
            dp[i][j] = j // coin[i]
        else:
            if j - coin[i] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coin[i]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]
# print(dp)
if dp[n][k] == 1e9:
    print(-1)
else:
    print(dp[n][k])