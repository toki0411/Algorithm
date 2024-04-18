import sys
sys.stdin.readline
N = int(input())
job = [ list(map(int,input().split())) for _ in range(N)]
dp = [0] * (N+1)

# 초기화
for i in range(N-1, -1, -1):
    day, price = job[i][0], job[i][1]
    if i + day > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + job[i][0]] + job[i][1])

print(dp[0])