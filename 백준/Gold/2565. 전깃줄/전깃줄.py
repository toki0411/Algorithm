n = int(input())
line = []
dp = [1 for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    line.append([a,b])
line.sort(key = lambda x: x[0])
ans = 0

#최장 증가 수열
for i in range(1, n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
ans =max( max(dp), ans)

print(n - ans)