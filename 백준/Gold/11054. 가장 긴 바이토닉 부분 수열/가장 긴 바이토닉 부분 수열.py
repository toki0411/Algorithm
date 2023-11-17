n = int(input())
num = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[j]+1, dp[i])
dp2 = [1] * n
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if num[i] > num[j]:
            dp2[i] = max(dp2[j]+1, dp2[i])

ans =0
for i in range(n):
    ans = max(dp[i] + dp2[i] - 1, ans)
print(ans)