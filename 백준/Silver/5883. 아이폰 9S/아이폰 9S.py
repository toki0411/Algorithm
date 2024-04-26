N = int(input())
p = [int(input()) for _ in range(N)]

num = []
for i in range(N):
    if p[i] not in num:
        num.append(p[i])

ans = 0
for j in range(len(num)):
    k = num[j]
    cnt = 0
    idx = 0
    while True:
        if p[idx] == k:
            idx += 1
        else:
            prev = p[idx]
            break

    for i in range(1, N):
        if p[i] == k:
            continue
        elif p[i] == prev:
            cnt += 1
        else:
            prev = p[i]
            cnt = 1
        ans = max(cnt, ans)
print(ans)
