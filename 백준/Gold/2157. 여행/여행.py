import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int,input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
dp = [[0] * (M+1) for _ in range(N+1)]

for _ in range(K):
    a, b, cost = map(int, input().split())
    if b < a:
        continue
    arr[a][b] = max(cost, arr[a][b])

q = deque()
q.append((1,1))
while q:
    now, cnt = q.popleft()
    if cnt + 1 > M:
        continue
    for i in range(1, N+1):
        cost = arr[now][i]
        if cost == 0:
            continue
        if dp[i][cnt + 1] < dp[now][cnt] + cost:
            dp[i][cnt+1] = dp[now][cnt] + cost
            q.append((i, cnt + 1))
ans = 0
for c in range(1, M+1):
    ans = max(dp[N][c], ans)
print(ans)
# 3 3 5
# 1 3 5
# 1 2 10
# 2 3 3
# 1 3 4
# 3 1 100