from bisect import *
n, m = map(int, input().split())
cake = list(map(int, input().split()))
cut = 0; ans = 0; cake.sort()
for i in range(len(cake)):
    if cake[i] == 10:
        ans += 1
        cake[i] = 0
    elif cake[i] % 10 == 0:
        ans += cake[i] // 10
        cut += (cake[i] // 10) - 1
        cake[i] = 0
    if cut > m:
        ans -= (cut - m+1)
        cut = m
        break
cake.sort()
cake = cake[bisect_left(cake, 1):]
for i in range(len(cake)):
    cut += cake[i] // 10
    ans += cake[i] // 10
    if cut > m:
        ans -= (cut - m)
        cut = m
        break

print(ans)