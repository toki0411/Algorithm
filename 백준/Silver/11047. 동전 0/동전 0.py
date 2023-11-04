n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True); ans = 0
for c in coin:
    if c <= k:
        ans += (k // c)
        k -= (k // c) * c

print(ans)
