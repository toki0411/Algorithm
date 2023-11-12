
n = int(input())
dp = [i for i in range(0, n+1)]
limit = int(n**0.5)
for i in range(2, limit+1):
    for j in range(i*i, n+1):
        dp[j] = min(dp[j], dp[j-i*i]+1)
print(dp[n])