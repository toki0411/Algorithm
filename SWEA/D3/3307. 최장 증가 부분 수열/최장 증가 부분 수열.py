t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    num = list(map(int, input().split()))
    dp = [1] * n
    for i in range(n):
        for j in range(0, i):
            if num[i] > num[j]:
                dp[i] = max(dp[i], dp[j]+1)

    print('#{} {}'.format(tc, max(dp)))
