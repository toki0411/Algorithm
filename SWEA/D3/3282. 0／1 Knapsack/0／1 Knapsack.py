t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    data = [[0,0]]
    for _ in range(n):
        data.append(list(map(int, input().split())))

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            weight, value = data[i][0], data[i][1]
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    print('#{} {}'.format(tc, dp[n][k]))
