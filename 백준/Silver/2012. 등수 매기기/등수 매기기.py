N = int(input())
estimated_rank = [int(input()) for _ in range(N)]
estimated_rank.sort()
ans = 0
for i in range(1, N+1):
    ans += abs(estimated_rank[i-1] - i )

print(ans)