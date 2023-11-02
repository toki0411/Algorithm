t = int(input())

for tc in range(1, t + 1):
    price = list(map(int,input().split()))
    plan = [0]+list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1,13):
        dp[i] = min(dp[i-1] + plan[i]*price[0], dp[i-1] + price[1])
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + price[2])

    print('#{} {}'.format(tc, min(dp[-1], price[2])))
