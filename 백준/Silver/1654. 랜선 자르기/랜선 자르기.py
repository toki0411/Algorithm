def cut(mid):
    tmp = 0
    for i in range(K):
        tmp += (line[i] // mid)
    return tmp
K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]
left = 1
right = max(line)
ans = 1
while left <= right:
    mid = (left + right) // 2
    cnt = cut(mid)  #자른 랜선의 길이, 자른 랜선의 개수
    if cnt < N:
        right = mid - 1
    elif cnt >= N:
        if mid > ans:
            ans = mid
        left = mid + 1
print(ans)