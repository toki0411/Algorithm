n = int(input())
stamina = [0]+list(map(int, input().split()))
joy = [0]+list(map(int, input().split()))
dp = [[0] * 101 for _ in range(len(stamina))]

for i in range(1, len(stamina)):
    for j in range(1, 100):
        st = stamina[i]
        jo = joy[i]
        if j < st:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-st] + jo)
print(dp[len(stamina)-1][99])
