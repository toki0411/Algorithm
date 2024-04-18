N = int(input())
price = list(map(int, input().split()))
dp = [0] * N
dp[0] = price[0]
ans = 0
for i in range(1, N):
    if price[i] < dp[i-1]:
        dp[i] = price[i]
    else:
        dp[i] = dp[i-1]
    if dp[i] < price[i]:
        ans = max(price[i] - dp[i], ans)
print(ans)