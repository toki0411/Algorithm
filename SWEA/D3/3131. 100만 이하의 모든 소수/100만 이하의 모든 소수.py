n = 1000000
dp = [i for i in range(1000001)]

for i in range(2, n+1):
    for j in range(i+i, n+1, i):
        if dp[j] != 0:
            dp[j] = 0

for i in range(2, n+1):
    if dp[i] != 0:
        print(dp[i], end = ' ')
