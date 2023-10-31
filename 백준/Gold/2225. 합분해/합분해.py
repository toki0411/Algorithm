n, k = map(int, input().split())
dp = [[0 for j in range(201)] for i in range(201)]

if k ==1:
    print(1)
elif k==2:
    print(n+1)
else:
    k = k-2
    for i in range(n + 1):
        dp[0][i] = (n + 1) - i
    cnt = 0

    while cnt != k:
        cnt += 1
        for i in range(n+1):
            if i==0:
                dp[cnt][i] = sum(dp[cnt - 1])
            else :
                dp[cnt][i] = dp[cnt][i-1] - dp[cnt-1][i-1]

    print(sum(dp[cnt-1])%1000000000)

