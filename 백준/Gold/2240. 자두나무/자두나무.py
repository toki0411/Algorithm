T, W = map(int, input().split())
berry = [int(input()) for _ in range(T)]
dp = [[[0] * (W + 2) for _ in range(3)] for __ in range(T)]  # 열매의 위치, 자두의 위치, 자두가 움직일 수 있는 횟수
# 1의 위치에서 시작
if berry[0] == 1:
    dp[0][1][0] = 1
else:
    dp[0][2][1] = 1

for i in range(1, T):
    for j in range(W + 1):
        if berry[i] == 1:
            dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][2][j - 1]) + 1
            dp[i][2][j] = max(dp[i - 1][2][j], dp[i - 1][1][j - 1])
        else:
            dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][2][j - 1])
            dp[i][2][j] = max(dp[i - 1][2][j], dp[i - 1][1][j - 1]) + 1
    # print(dp)

ans = -1
# print(dp)

for w in range(W+1):
    ans = max(ans, max(dp[T-1][1][w], dp[T-1][2][w]))
print(ans)