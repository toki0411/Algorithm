t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    s = 0
    k = 1
    arr = [[0] * n for _ in range(n)]
    while n > 0:
        last = s + n -1
        for i in range(s, last+1):
            arr[s][i] = k
            k += 1
        for i in range(s + 1, last+1):
            arr[i][last] = k
            k += 1
        for i in range(last-1, s-1, -1):
            arr[last][i] = k
            k += 1
        for i in range(last-1, s, -1):
            arr[i][s] = k
            k += 1
        n -= 2
        s += 1
    print('#{} '.format(tc))
    for p in arr:
        print(*p)
