import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline
def fibonacci(x):
    if dp[x] != 0:
        return dp[x]
    if x == 0:
        return 0
    dp[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return dp[x]

n = int(input())
dp = [0 for i in range(10001)]
dp[0] = 0
dp[1] = 1
fibonacci(n)
print(dp[n])