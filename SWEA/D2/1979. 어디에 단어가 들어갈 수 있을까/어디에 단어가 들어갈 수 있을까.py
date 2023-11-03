from collections import deque
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for tc in range(1, t + 1):
    n, k = map(int, input().split()); ans = 0
    graph = [list(map(int, input().split())) for _ in range(n)]
    #가로
    for i in range(n):
        cnt = 0; val = 0
        for j in range(n):
            if graph[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1

    #세로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans +=1
                cnt = 0
        if cnt == k:
            ans += 1

    print('#{} {}'.format(tc, ans));

