import sys

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
limit = sum(cost)
dp = [[0] * (limit + 1) for _ in range(n + 1)]
ans = 1e9

for i in range(1, n + 1):

    for j in range(limit + 1):
        mem = memory[i]
        c = cost[i]
        if j < cost[i]:  # 현재 앱을 비활성화할만큼의 cost가 충분하지 않은 경우
            dp[i][j] = dp[i-1][j]
        else:  # 같은 cost 내에서 현재 앱을 끈 뒤의 byte와 현재 앱을 끄지 않은 뒤의 byte를 비교
            dp[i][j] = max(dp[i - 1][j - c] + mem, dp[i - 1][j])
        if dp[i][j] >= m:
            ans = min(ans, j)
print(ans)