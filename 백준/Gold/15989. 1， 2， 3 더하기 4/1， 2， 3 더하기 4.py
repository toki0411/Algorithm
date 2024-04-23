t = int(input())
limit = 10_000
dp = [0] * 10001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 5
for i in range(6, limit + 1):
    dp[i] = dp[i-3] + dp[i-2] - dp[i-5] + 1

for tc in range(t):
    num = int(input())
    print(dp[num])