n, m, k = map(int, input().split())
cnt = 0
while True:
    if n-2 >=0 and m-1 >= 0 and (n-2) + (m-1) >= k:
        cnt += 1
        n -= 2
        m -= 1
    else:
        break
print(cnt)

