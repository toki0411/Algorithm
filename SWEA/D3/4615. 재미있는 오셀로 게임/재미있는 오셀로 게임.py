t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    graph[n // 2 - 1][n // 2 - 1] = 2;
    graph[n // 2 - 1][n // 2] = 1
    graph[n // 2][n // 2 - 1] = 1;
    graph[n // 2][n // 2] = 2
    for mm in range(m):
        x, y, c = map(int, input().split())
        x = x - 1;
        y = y - 1
        graph[x][y] = c;
        for dx, dy in ((-1,-1),(-1,1),(1,1),(-1,0),(1,0),(0,1),(0,-1),(1,-1)):
            arr = []
            for i in range(1,n):
                nx, ny = x + i*dx, y + i*dy
                if 0<= nx < n and 0<= ny < n:
                    if graph[nx][ny] == 0:
                        break
                    elif graph[nx][ny] == c: #같은 바둑돌
                        while arr:
                            tx, ty = arr.pop()
                            graph[tx][ty] = c
                        break
                    else:
                        arr.append([nx, ny])
                else:
                    break
        bcnt = wcnt = 0
        for g in graph:
            bcnt += g.count(1)
            wcnt += g.count(2)

    print('#{}'.format(tc), bcnt, wcnt)

