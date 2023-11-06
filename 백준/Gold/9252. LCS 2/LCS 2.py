n = list(' '+input())
m = list(' '+input())
dp = [[""] * len(m) for _ in range(len(n))];
for i in range(1, len(n)):
    for j in range(1, len(m)):
        if n[i] == m[j]:
            dp[i][j] = dp[i-1][j-1]+n[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

if len(dp[-1][-1]) == 0:
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])

