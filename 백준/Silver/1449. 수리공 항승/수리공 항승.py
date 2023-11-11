n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()
ans = 0
visited= [-1] * n

for i in range(n):
    if visited[i]==-1:
        for j in range(i, n):
            if leak[i]-0.5 + l > leak[j]:
                visited[j] = i

val = -1
for i in visited:
    if i != val:
        ans += 1
        val = i
print(ans)