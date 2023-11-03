n, k = map(int, input().split())
atmosphere = list(map(int, input().split()))
val = sum(atmosphere[:k]); ans = sum(atmosphere[:k])
for i in range(1, n-k+1):
    val = val - atmosphere[i-1] + atmosphere[i+k-1]
    ans = max(ans, val)
print(ans)