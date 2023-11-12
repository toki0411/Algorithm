t = int(input())
for tc in range(1, t+1):
    station = [0] * (5001)
    n = int(input()); ans = []
    bus = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(bus[i][0], bus[i][1]+1):
            station[j] += 1

    p = int(input())
    for _ in range(p):
        v = int(input())
        ans.append(station[v])

    print('#{} '.format(tc), end = '')
    print(*ans[:])

