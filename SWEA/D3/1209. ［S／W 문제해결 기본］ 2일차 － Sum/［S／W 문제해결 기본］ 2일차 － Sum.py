
for tc in range(1, 11):
    t = int(input()); ans = 0; n = 100
    arr = [list(map(int , input().split())) for _ in range(100)]
    # 왼쪽 대각선
    val = 0
    for i in range(n):
        val += arr[i][i]
    ans = max(val, ans)

    # 오른쪽 대각선
    val = idx = 0
    for i in range(n-1,-1,-1):
        val += arr[i][idx]
        idx += 1
    ans = max(val, ans)

    #가로
    for i in range(n):
        ans = max(sum(arr[i]), ans)
    #세로
    reversed_arr = arr[::-1]
    rotated = list(zip(*reversed_arr))
    for i in range(n):
        ans = max(sum(rotated[i]), ans)

    print('#{} {}'.format(t, ans))
