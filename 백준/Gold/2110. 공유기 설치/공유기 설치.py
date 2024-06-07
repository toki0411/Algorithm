N, C = map(int, input().split())
router = []
for _ in range(N):
    a = int(input())
    router.append(a)

router.sort()

left = 1 #공유기 사이의 거리
right = router[-1] - router[0]
ans = 0
while left <= right:
    mid = (left + right) // 2
    key = False
    cnt = 1
    val = 0
    for i in range(1, N): #첫번째 공유기는 이미 설치되었다고 생각한다.
        # print(mid, val, cnt)
        val += router[i] - router[i-1]
        if val >= mid:
            cnt += 1
            val = 0

    if cnt >= C:
        ans = max(mid, ans)
        left  = mid + 1
    else:
        right = mid - 1

print(ans)