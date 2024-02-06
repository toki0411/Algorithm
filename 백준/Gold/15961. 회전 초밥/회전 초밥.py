import sys

n, d, k, c = map(int, input().split())
sushi = [int(sys.stdin.readline()) for _ in range(n)]
s = set()
cnt = [0] * (d + 1)
for i in range(k):
    cnt[sushi[i]] += 1
    if sushi[i] not in s:
        s.add(sushi[i])
start = 0
end = k
ans = len(s)
for i in range(n):
    if end >= n:
        end = 0
    cnt[sushi[start]] -= 1
    cnt[sushi[end]] += 1
    if cnt[sushi[start]] <= 0:
        s.remove(sushi[start])
    if sushi[end] not in s:
        s.add(sushi[end])
    if c in s:
        ans = max(ans, len(s))
    else:
        ans = max(ans, len(s) + 1)

    start += 1
    end += 1

print(ans)