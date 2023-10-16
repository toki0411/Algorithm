import sys
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
    idx = i + k
    if idx >= n:
        idx -= n
        tmp = set(sushi[i:] + sushi[:idx])
        if c not in tmp:
            tmp.add(c)
            ans = max(len(tmp), ans)
        else:ans = max(len(tmp), ans)
    else:
        tmp = set(sushi[i:idx])
        if c not in tmp:
            tmp.add(c)
            ans = max(len(tmp), ans)
        else:
            ans = max(len(tmp), ans)

print(ans)

