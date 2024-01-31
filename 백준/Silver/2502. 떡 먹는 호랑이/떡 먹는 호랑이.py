d, k = map(int, input().split())
dp = [0] * (d+1)
dp[d] = k

d1= d2 = 1
while True:
    dp[0] = d1; dp[1] = d2;
    for i in range(2, d):
        dp[i] = dp[i-1] + dp[i-2]

    if dp[d-1] == k:
        print(d1)
        print(d2)
        break;
    else:
        if dp[d-1] < k:
            d2 +=1
        else:
            d1+=1
            d2 = d1

