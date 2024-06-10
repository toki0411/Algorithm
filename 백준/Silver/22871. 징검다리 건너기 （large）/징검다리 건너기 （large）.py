n = int(input())
stone = list(map(int, input().split()))

dp = [0] * n
for i in range(1,n):
    min_val = 1e8
    for j in range(i):
        power = (i-j) * (1+abs(stone[i] - stone[j]))  #j에서 i까지 가는 데 드는 힘
        val = max(dp[j], power)
        if val < min_val:
            min_val = val
    dp[i] = min_val
# print(dp)
print(dp[n-1])